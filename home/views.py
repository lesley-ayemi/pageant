import os

# import stripe
from contestants.models import ContestType, ContestantForm
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from home.forms import ContactForm, RegisterForm
from django.core.mail import EmailMessage

from home.models import Gallery
from django.contrib import messages



class SuccessView(TemplateView):
    template_name = "success.html"
    
class CancelView(TemplateView):
    template_name = "cancel.html"

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'home/about.html')
    
class ContactUsView(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form':form
        }
        return render(request, 'home/contact.html', context)
    
    def post(self, request):
        # name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        #send email
        email = EmailMessage(
            subject,
            message,
            email, 
            settings.EMAIL_HOST_USER,
        )
        
        
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        c_types = ContestType.objects.all()
        context = {'form':form, 'c_types':c_types}
        return render(request, 'home/apply.html', context)
    
    def post(self, request):
        c_types = ContestType.objects.all()
        context = {'c_types':c_types, 'values':request.POST}
        
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        state_of_origin = request.POST['state_of_origin']
        state_of_residence = request.POST['state_of_residence']
        reg_type = request.POST['reg_type']
        address = request.POST['address']
        reg_image = request.FILES['reg_image']
        
        contest_type = ContestType.objects.get(id=reg_type)
        
        if not name:
            messages.error(request, 'Please Enter Your Name')
            return render(request, 'home/apply.html', context)
        
        if not phone_no:
            messages.error(request, 'Phone Number is required')
            return render(request, 'home/apply.html', context)
        
        if not state_of_origin:
            messages.error(request, 'State of origin is required')
            return render(request, 'home/apply.html', context)
        
        if not state_of_residence:
            messages.error(request, 'State of residence is required')
            return render(request, 'home/apply.html', context)
        
        if not reg_type:
            messages.error(request, 'Select A contest')
            return render(request, 'home/apply.html', context)
        
        if not address:
            messages.error(request, 'Address is required')
            return render(request, 'home/apply.html', context)
        
        if not reg_image:
            messages.error(request, 'Upload A Photo')
            return render(request, 'home/apply.html', context)
        
        ContestantForm.objects.create(name=name, phone_no=phone_no, state_of_origin=state_of_origin, state_of_residence=state_of_residence, reg_type=contest_type, address=address, reg_image=reg_image)
        messages.success(request, 'Registration Filled Successfully')
        return redirect('index')
        

class GalleryView(TemplateView):
    template_name = 'home/gallery.html'
    
    def get_context_data(self, *args, **kwargs):
        galleries = Gallery.objects.all()
        context = ({
            'galleries':galleries,
        })
        return context
        
    
class AllContestantsView(View):
    def get(self, request):
        contestants = ContestantForm.objects.all()
        context = {
            'all_contestants':contestants,
        }
        return render(request, 'home/contestants/all-contestants.html', context)

# class ContestantView(View):
#     def get(self, request, pk):
#         data = ContestantForm.objects.get(id=pk)
#         form = PaymentForm()
#         context = {
#             'contestant':data,
#             'form':form,
#             'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
#         }
#         return render(request, 'home/contestants/contestant-detail.html', context)

#     def post(self, request, pk):
#         pass
        # data = ContestantForm.objects.get(id=pk)
        # form = PaymentForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     email = form.cleaned_data['email']
        #     amount = form.cleaned_data['amount']
        #     phone = form.cleaned_data['phone']
        #     return redirect(str(process_payment(name,email,amount,phone)))

class ContestantView(TemplateView):
    template_name = "home/contestants/contestant-detail.html"

    def get_context_data(self, pk, **kwargs):
        contestant = ContestantForm.objects.get(id=pk)
        context = super(ContestantView, self).get_context_data(**kwargs)
        context.update({
            "contestant": contestant,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context

import stripe
stripe.api_key = "sk_test_51H2Hm2EMcQisWvWMHv6wIW0auJmBrvnxBQa3fLiL875grQLh46jq19EcXNpAHC55Iioc7X5ofccBmqEvTbsdYbuL000FqJlhO9"

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        contestant_id = self.kwargs["pk"]
        contestant = ContestantForm.objects.get(id=contestant_id)
        print(contestant)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[

                {
                    'price_data': {
                        'currency': 'ngn',
                        'unit_amount': contestant.amount,
                        'product_data': {
                            'name': contestant.name
                        },
                    },
                    'quantity': 1,
                },
            ],

            mode='payment',

            success_url=YOUR_DOMAIN + '/success/',

            cancel_url=YOUR_DOMAIN + '/cancel/',

        )
        return JsonResponse({'id': checkout_session.id})
