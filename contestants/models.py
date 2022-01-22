from unicodedata import name
from django.db import models

# Create your models here.
class ContestType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ContestantForm(models.Model):
    REG_STATUS = (
        ('pending', 'PENDIND'),
        ('approved', 'APPROVED'),
    )
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    reg_email = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    reg_type = models.ForeignKey(to=ContestType, on_delete=models.CASCADE)
    reg_image = models.FileField(upload_to='media/uploads/registration_images/', null=True, blank=True)
    amount = models.PositiveIntegerField(default=500)
    status = models.CharField(choices=REG_STATUS, default='PENDING', max_length=15)
    likes = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=0)
    date_reg = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name