from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="Prénom de l'auteur", max_length=100)
    last_name = forms.CharField(label="Nom de l'auteur", max_length=100)
    birth_date = forms.DateField(label="Date de naissance", widget=forms.DateInput(attrs={'type': 'date'}))
    nationality = forms.CharField(label="Nationalité", max_length=50)
    biography = forms.CharField(label="Biographie", required=False, widget=forms.Textarea)
    death_date = forms.DateField(label="Date de décès", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    website = forms.URLField(label="Site web", required=False)
    photo = forms.FileField(label="Photo", required=False)