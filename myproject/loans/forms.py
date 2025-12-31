from django import forms
from .models import Loan
import datetime

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan # Le modèle associé au formulaire
        fields = ['name_loaner', 'email_loaner', 'library_card_number', 'return_date', 'status', 'commentary_librarian', 'book'] # Champs à inclure dans le formulaire
        widgets = {
            'name_loaner': forms.TextInput(attrs={'class': 'form-control'}),
            'email_loaner': forms.EmailInput(attrs={'class': 'form-control'}),
            'library_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'return_date': forms.DateTimeInput(attrs={'class': 'form-control', 
                                                      'type': 'datetime-local', 
                                                      'value': (datetime.datetime.now() + datetime.timedelta(days=14)).strftime('%Y-%m-%dT%H:%M')}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'commentary_librarian': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'book': forms.Select(attrs={'class': 'form-control'}),
        } # Widgets personnalisés pour certains champs
        
    def clean(self):
        """
        Validation personnalisée pour le formulaire de prêt.
        """
        cleaned_data = super().clean()
        
        self.clean_loaner_more_than_five_loans(cleaned_data)
        self.clean_copies_available(cleaned_data)
        
    def clean_loaner_more_than_five_loans(self, cleaned_data):
        """
        Valide que l'emprunteur n'a pas plus de 5 prêts en cours.
        """
        name_loaner = cleaned_data.get('name_loaner')
        email_loaner = cleaned_data.get('email_loaner')
        library_card_number = cleaned_data.get('library_card_number')
        
        if name_loaner and email_loaner and library_card_number:
            existing_loans = Loan.objects.filter(
                name_loaner=name_loaner,
                email_loaner=email_loaner,
                library_card_number=library_card_number,
                status='en_cours'
            ).count()
            
            if existing_loans >= 5:
                raise forms.ValidationError("Un emprunteur ne peut pas avoir plus de 5 prêts en cours.")
            
    def clean_copies_available(self, cleaned_data):
        """
        Valide qu'il y a des copies disponibles pour le livre emprunté.
        """
        book = cleaned_data.get('book')
        
        if book:
            if book.copies_available <= 0:
                raise forms.ValidationError("Aucune copie disponible pour ce livre. Impossible d'emprunter ce livre.")
        