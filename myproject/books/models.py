from django.db import models
from authors.models import Author

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    
    # ForeignKey to Author model (assuming an Author model exists)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    def get_published_date(self):
        return self.published_date
    
    def set_title(self, new_title):
        self.title = new_title
        self.save()
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        self.save()
    def set_author(self, new_author):
        self.author = new_author
        self.save()
    def set_price(self, new_price):
        self.price = new_price
        self.save()
    def set_published_date(self, new_date):
        self.published_date = new_date
        self.save()
