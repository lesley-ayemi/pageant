from unicodedata import name
from django.db import models

# Create your models here.
class ContestType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(name)

class ContestantForm(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    reg_email = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    reg_type = models.ForeignKey(to=ContestType)
    reg_image = models.FileField(upload_to='uploads/registration_images/', null=True, blank=True)
    amount = models.PositiveIntegerField(default=500)
    likes = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=0)
    date_reg = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)