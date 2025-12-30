from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_image(self):
        return self.image
    
    def set_name(self, new_name):
        self.name = new_name
        self.save()
    def set_description(self, new_description):
        self.description = new_description
        self.save()
    def set_image(self, new_image):
        self.image = new_image
        self.save()
        