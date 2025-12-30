from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'isbn', 'title', 'price', 'published_date', 'copies_available',
            'copies_possessed', 'description', 'language', 'number_pages',
            'edition', 'author', 'category', 'image'
        ]
        
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'author': forms.Select(),
            'category': forms.Select(),
        }
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price < 0:
            raise forms.ValidationError("Le prix ne peut pas être négatif.")
        return price
    
    def clean_copies_available(self):
        copies_available = self.cleaned_data.get('copies_available')
        if copies_available and copies_available < 0:
            raise forms.ValidationError("Le nombre de copies disponibles ne peut pas être négatif.")
        return copies_available
