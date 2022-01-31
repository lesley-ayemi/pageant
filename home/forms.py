from django import forms

from contestants.models import ContestantForm

# class PaymentForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=15)
#     amount = forms.FloatField()
    
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.Textarea()