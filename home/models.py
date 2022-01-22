import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.email}"