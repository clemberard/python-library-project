from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author # Le modèle associé au formulaire
        fields = [
            'first_name', 'last_name', 'birth_date', 'nationality', 'biography',
            'death_date', 'website', 'photo'
        ] # Champs à inclure dans le formulaire
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'death_date': forms.DateInput(attrs={'type': 'date'}),
            'biography': forms.Textarea(attrs={'rows': 4}),
        } # Widgets personnalisés pour certains champs
        
    def clean(self):
        cleaned_data = super().clean()
        
        # Validation personnalisée pour les dates
        if 'birth_date' in cleaned_data and 'death_date' in cleaned_data: 
            self.clean_dates()
            
        # Validation personnalisée pour les noms uniques
        if 'first_name' in cleaned_data and 'last_name' in cleaned_data:
            self.clean_unique_names()
            
    def clean_dates(self):
        """
        Valide que la date de décès n'est pas antérieure à la date de naissance.
        """
        birth_date = self.cleaned_data.get('birth_date')
        death_date = self.cleaned_data.get('death_date')
        if birth_date and death_date and death_date < birth_date:
            raise forms.ValidationError("La date de décès ne peut pas être antérieure à la date de naissance.")
        return death_date

    def clean_unique_names(self):
        """
        Valide que la combinaison prénom/nom est unique.
        """
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if first_name and last_name:
            existing_authors = self.Meta.model.objects.filter(first_name=first_name, last_name=last_name)
            if existing_authors.exists():
                raise forms.ValidationError("Un auteur avec ce prénom et ce nom existe déjà.")
        return first_name, last_name