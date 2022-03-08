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
    

class Gallery(models.Model):
    g_images = models.ImageField(upload_to='media/uploads/gallery/', null=True)
    captions = models.CharField(max_length=255, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['-g_images']
        verbose_name = 'gallery'
        verbose_name_plural = 'gallery images'
    
    def __str__(self) -> str:
        return f"{self.pk} - {self.g_images}"
    
    