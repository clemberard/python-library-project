from django.db import models
from books.models import Book

# Create your models here.

class Loan(models.Model):
    name_loaner = models.CharField(max_length=100)
    email_loaner = models.EmailField()
    library_card_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('en_cours', 'En cours'),
        ('retourne', 'Retourné'),
        ('en_retard', 'En retard')
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    commentary_librarian = models.TextField(blank=True, null=True)
    
    # foreign keys
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Loan of '{self.book.title}' to {self.name_loaner}"
    
    def get_name_loaner(self):
        return self.name_loaner
    def get_email_loaner(self):
        return self.email_loaner
    def get_library_card_number(self):
        return self.library_card_number
    def get_created_at(self):
        return self.created_at
    def get_return_date(self):
        return self.return_date
    def get_status(self):
        return self.status
    def get_commentary_librarian(self):
        return self.commentary_librarian
    def get_book(self):
        return self.book
    
    def set_name_loaner(self, new_name_loaner):
        self.name_loaner = new_name_loaner
        self.save()
    def set_email_loaner(self, new_email_loaner):
        self.email_loaner = new_email_loaner
        self.save()
    def set_library_card_number(self, new_library_card_number):
        self.library_card_number = new_library_card_number
        self.save()
    def set_return_date(self, new_return_date):
        self.return_date = new_return_date
        self.save()
    def set_status(self, new_status):
        self.status = new_status
        self.save()
    def set_commentary_librarian(self, new_commentary_librarian):
        self.commentary_librarian = new_commentary_librarian
        self.save()
    def set_book(self, new_book):
        self.book = new_book
        self.save()
