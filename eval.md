# Évaluation

## Question 1

### Partie A

```python
# Course
from django.db import models
from instructors.models import Instructor

class Course(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duree = models.IntegerField(default=0) # en minutes
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    date_creation = models.DateField()
    STATUS_CHOIX = [
        ('brouillon', 'Brouillon'),
        ('publie', 'Publié'),
        ('archive', 'Archivé')
    ]
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='brouillon')
    
    # foreign keys
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre

    def get_prix_ttc(self, taux_tva):
        return self.prix * (1 + taux_tva / 100)
```

```python
# Instructor
from django.db import models

class Instructor(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biographie = models.TextField(blank=True, null=True)
    photo_profil = models.ImageField(blank=True, null=True)
    date_inscription = models.DateField()

    def __str__(self):
        return self.nom

    def get_nombre_cours(self):
        return self.course_set.count()
```

```python
# Enrollment
from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Enrollment(models.Model):
    date_inscription = models.DateField()
    date_completion = models.DateField(blank=True, null=True)
    note_finale = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    statut_CHOICES = [
        ('en_cours', 'En cours'),
        ('complete', 'Complété'),
        ('abandonné', 'Abandonné')
    ]
    statut = models.CharField(max_length=20, choices=statut_CHOICES, default='en_cours')

    # foreign keys
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.course.titre}"

    def is_complete(self):
        return self.statut == 'complete'
```

### Partie B

```python
1. Course.objects.all().order_by('prix')
2. Enrollment.objects.get(id=5).user
3. Enrollment.objects.filter(statut='complete', course__instructor__id=X).count()
4. Enrollment.objects.order_by('course').distinct('user')[:3]
```

### Partie C

1. Django implémente le design pattern MVT pour Model Vue Template. Le modèle gère les données et la logique métier (comme un modèle dans un MVC), la vue traite les requêtes et renvoie les réponses (joue le rôle de contrôleur dans un MVC), et le template gère la présentation des données (comme la vue dans un MVC).

2. La différence entre le MVT et le MVC est que dans le MVT, la vue est responsable de la logique de traitement des requêtes et des réponses, tandis que dans le MVC, le contrôleur gère cette logique. Il y aussi le routage des URL qui est géré par URL dispatcher dans Django, contrairement à un router classique dans MVC.

3. Un avantage d'Active Record dans Django est la simplicité d'utilisation et le fait que le modèle soit lié à une table de la bdd, ca facilite les opérations CRUD.
Un inconvénient est que ca entraine des problèmes de performance car chaque modèle est directement lié à une table.

## Question 2

### Partie A

```python
# forms.py
from django import forms
from .models import Enrollment, User, Course

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        # Changer le modele Enrollment pour inclure l'email et le texte de motivation (j'espere que tu ne m'en vludras pas si je ne le fais pas :) )
        fields = ['course', 'user', 'date_inscription', 'statut', 'email', 'texte_motivation']
        widgets = {
            'date_inscription': forms.DateInput(attrs={'type': 'date'}),
            'statut': forms.Select(choices=Enrollment.statut_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()

        self.clean_places_disponibles()

        self.clean_user_deja_inscrit()

        self.clean_email()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domaine_autorise = '@student.edu'
        if domaine_autorise not in email:
            raise forms.ValidationError('L\'email doit appartenir au domaine student.edu.')
        return email

    def clean_places_disponibles(self):
        course = self.cleaned_data.get('course')
        if course:
            nombre_inscriptions = Enrollment.objects.filter(course=course).count()
            places_disponibles = 30
            if nombre_inscriptions >= places_disponibles:
                raise forms.ValidationError('Il n\'y a plus de places disponibles pour ce cours.')

    def clean_user_deja_inscrit(self):
        user = self.cleaned_data.get('user')
        course = self.cleaned_data.get('course')
        if user and course:
            inscription_existante = Enrollment.objects.filter(user=user, course=course).exists()
            if inscription_existante:
                raise forms.ValidationError('Cet utilisateur est déjà inscrit à ce cours.')
```

### Partie B

```python
# views.py
from django.shortcuts import render
from .forms import EnrollmentForm

def new_loan(request):
    """
    Affiche le formulaire pour créer une nouvelle inscription à un cours.
    Args:
        request (HttpRequest): L'objet de requête HTTP.
    Returns:
        Rendered HTML page pour créer une nouvelle inscription.
    """

    form = EnrollmentForm()

    return render(request, 'enrollments/new.html', {'form': form})

def create_enrollment(request):
    """
    Traite le formulaire de création d'une nouvelle inscription à un cours.
    Args:
        request (HttpRequest): L'objet de requête HTTP.
    Returns:
        Rendered HTML page après la création d'une nouvelle inscription.
    """

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courses/index.html', {
                'message': 'Inscription réussie au cours !'
            })
        else:
            return render(request, 'enrollments/new.html', {'form': form})

```

```html
<!-- Template: enrollments/new.html -->
<h2>Inscription à un cours</h2>
<form method="post">
    {% csrf_token %}
    {% if form.errors %}
        <div class="errors">
            {{ form.errors }}
        </div>
    {% endif %}
    {{ form }}
    <input type="checkbox" name="terms" required> J'accepte les conditions
    <button type="submit">S'inscrire</button>
</form>
```

### Partie C

1. Le Pattern Post Redirect Get est un pattern permettant de ne pas avoir de soumissions multiples. Il fonctionne notamment avec la requete POST qui est retourné en en-tete de redirection.

2. Le jeton CSRF est un jeton unique et aléatoire qui est génére par le serveur. Ca permet une protection contre des attaque CSRF.

## Question 3

### Partie A

```python
# StudentProfile
from django.db import models
from django.contrib.auth.models import User

class StudentProfile(AbstractUser):
    numero_etudiant = models.IntegerField(unique=True)
    date_naissance = models.DateField()
    ETUDES_CHOIX = [
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat')
    ]
    niveau_etudes = models.CharField(max_length=20, choices=ETUDES_CHOIX, default='licence')
```

```python
# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            request,
            username=username,
            password=password
        )
        
        if user is not None:
            login(request, user)
            
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            error = "Identifiants invalides"
    else:
        error = None
    
    return render(request, 'login.html', {
        'error': error
    })
```

### Partie B

```python
# Dans une classe Meta situé dans le model Course

permissions = [
    ('can_publish_course', 'Peut publier un cours'),
    ('can_view_statistics', 'Peut voir les statistiques'),
]
```

```python
# views.py

from django.contrib.auth.decorators import login_required, permission_required
from courses.models import Course

@login_required
@permission_required('course.can_publish_course')
def course_publish(request, course_id):
    course = Course.objects.get(id=5)
    course.statut = 'publie'
    course.save()
```

### Partie C

```twig
{% if user.is_authenticated %}
    <p>{{ user.username }}</p>
    <a href="{% url 'logout' %}">Déconnexion</a>
{% endif %}

{% if perms.course.can_view_statistics %}
    <a href="{% url 'stats' book.pk %}">Statistiques</a>
{% endif %}

{% if perms.course.can_publish_course %}
    <button class="btn-danger">Publier</button>
{% endif %}
```
