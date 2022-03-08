import secrets
from unicodedata import name
from django.db import models

# Create your models here.
class ContestType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'contest type'

class ContestantForm(models.Model):
    REG_STATUS = (
        ('pending', 'PENDIND'),
        ('approved', 'APPROVED'),
    )
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    # reg_email = models.CharField(max_length=100)
    state_of_origin = models.CharField(max_length=200, null=True)
    state_of_residence = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    reg_type = models.ForeignKey(to=ContestType, on_delete=models.CASCADE)
    reg_image = models.FileField(upload_to='media/uploads/registration_images/', default='default.png', null=True, blank=True)
    amount = models.PositiveIntegerField(default=500)
    verified = models.BooleanField(default=False)
    status = models.CharField(choices=REG_STATUS, default='PENDING', max_length=15)
    likes = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=0)
    date_reg = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.amount / 100)
    
    class Meta:
        ordering = ['-date_reg']
        verbose_name_plural = 'All Contestant'
    
# class Payment(models.Model):
#     amount = models.PositiveIntegerField()
#     ref = models.CharField(max_length=200)
#     email = models.EmailField()
#     verified = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ('-date_created')
        
#     def __str__(self) -> str:
#         return f"Payment: {self.amount}"
    
#     def save(self, *args, **kwargs):
#         while not self.ref:
#             ref = secrets.token_urlsafe(50)
#             if not object_with_similar_ref:
#                 self.