from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    def get_birth_date(self):
        return self.birth_date
    def get_nationality(self):
        return self.nationality
    
    def set_name(self, new_name):
        self.name = new_name
        self.save()
    def set_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
        self.save()
    def set_nationality(self, new_nationality):
        self.nationality = new_nationality
        self.save()
        