from django import forms
from .models import Book

class LoanForm(forms.Form):
    name_loaner = forms.CharField(label="Nom de l'emprunteur", max_length=100)
    email_loaner = forms.EmailField(label="Email de l'emprunteur")
    library_card_number = forms.CharField(label="Numéro de carte de bibliothèque", max_length=50)
    return_date = forms.DateTimeField(label="Date de retour", required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    status = forms.CharField(label="Statut", max_length=100)
    commentary_librarian = forms.CharField(label="Commentaire du bibliothécaire", required=False, widget=forms.Textarea)
    book = forms.ModelChoiceField(
        queryset = Book.objects.all(),
        label="Livre",
        required=True
    )