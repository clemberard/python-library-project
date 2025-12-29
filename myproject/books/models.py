from django.db import models
from authors.models import Author
from categories.models import Category

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    copies_available = models.IntegerField(default=0)
    copies_possessed = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30)
    number_pages = models.IntegerField(default=0)
    edition = models.CharField(max_length=100, blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # foreign keys
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

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
    def get_copies_available(self):
        return self.copies_available
    def get_copies_possessed(self):
        return self.copies_possessed
    def get_description(self):
        return self.description
    def get_language(self):
        return self.language
    def get_number_pages(self):
        return self.number_pages
    def get_edition(self):
        return self.edition
    def get_image(self):
        return self.image
    def get_created_at(self):
        return self.created_at
    
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
    def set_copies_available(self, new_copies):
        self.copies_available = new_copies
        self.save()
    def set_copies_possessed(self, new_copies):
        self.copies_possessed = new_copies
        self.save()
    def set_description(self, new_description):
        self.description = new_description
        self.save()
    def set_language(self, new_language):
        self.language = new_language
        self.save()
    def set_number_pages(self, new_number):
        self.number_pages = new_number
        self.save()
    def set_edition(self, new_edition):
        self.edition = new_edition
        self.save()
    def set_image(self, new_image):
        self.image = new_image
        self.save()
    def set_created_at(self, new_created_at):
        self.created_at = new_created_at
        self.save()
