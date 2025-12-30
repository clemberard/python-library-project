from django import forms
from books.models import Book
import datetime

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

    def clean(self):
        cleaned_data = super().clean()
        
        if 'isbn' in cleaned_data:
            self.clean_size_isbn()
            
        if 'price' in cleaned_data:
            self.clean_price()
            
        if 'copies_available' in cleaned_data:
            self.clean_copies_available()

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
    
    def clean_size_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn and len(isbn) not in [10, 13]:
            raise forms.ValidationError("L'ISBN doit contenir 10 ou 13 caractères.")
        return isbn
    
    def clean_number_pages(self):
        number_pages = self.cleaned_data.get('number_pages')
        if number_pages and number_pages <= 0:
            raise forms.ValidationError("Le nombre de pages doit être un entier positif.")
        return number_pages
    
    def clean_books_available(self):
        copies_available = self.cleaned_data.get('copies_available')
        copies_possessed = self.cleaned_data.get('copies_possessed')
        if (copies_available is not None and copies_possessed is not None and
                copies_available > copies_possessed):
            raise forms.ValidationError("Le nombre de copies disponibles ne peut pas dépasser le nombre de copies possédées.")
        return copies_available
    
    def clean_year_published(self):
        published_date = self.cleaned_data.get('published_date')
        if published_date and published_date.year < 1450 and published_date > datetime.date.today():
            raise forms.ValidationError("L'année de publication doit être postérieure à 1450.")
        return published_date
