from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category # Le modèle associé au formulaire
        fields = ['name', 'description', 'image'] # Champs à inclure dans le formulaire
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        } # Widgets personnalisés pour certains champs
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        # Validation pour les noms uniques
        if name and Category.objects.filter(name__iexact=name).exists():
            self.add_error('name', 'Une catégorie avec ce nom existe déjà.')
        
        return cleaned_data