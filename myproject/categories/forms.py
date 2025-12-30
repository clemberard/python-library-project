from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        
        if name and Category.objects.filter(name__iexact=name).exists():
            self.add_error('name', 'Une catégorie avec ce nom existe déjà.')
        
        return cleaned_data