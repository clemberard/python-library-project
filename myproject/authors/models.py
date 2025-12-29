from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    biography = models.TextField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_birth_date(self):
        return self.birth_date
    def get_nationality(self):
        return self.nationality
    def get_biography(self):
        return self.biography
    def get_death_date(self):
        return self.death_date
    def get_website(self):
        return self.website
    def get_photo(self):
        return self.photo
    
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
        self.save()
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.save()
    def set_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
        self.save()
    def set_nationality(self, new_nationality):
        self.nationality = new_nationality
        self.save()
    def set_biography(self, new_biography):
        self.biography = new_biography
        self.save()
    def set_death_date(self, new_death_date):
        self.death_date = new_death_date
        self.save()
    def set_website(self, new_website):
        self.website = new_website
        self.save()
    def set_photo(self, new_photo):
        self.photo = new_photo
        self.save()
        