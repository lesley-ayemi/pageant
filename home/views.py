from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from contestants.models import ContestantForm
from home.forms import PaymentForm
import os
from django.views.decorators.http import require_http_methods
# import requests
# import environ

# env = environ.Env()
# environ.Env.read_env()

# Create your views here.
def process_payment(name, email,amount,phone):
    auth_token= os.environ.get('FLUTTER_SECRET_KEY')
    # auth_token= env('SECRET_KEY')
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
                "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
                "amount":amount,
                "currency":"KES",
                "redirect_url":"http://127.0.0.1:8000/callback",
                "payment_options":"card",
                "meta":{
                    "consumer_id":23,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":phone,
                    "name":name
                },
                "customizations":{
                    "title":"Supa Electronics Store",
                    "description":"Best store in town",
                    "logo":"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
                }
                }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link

@require_http_methods(['GET', 'POST'])
def payment_response(request):
    status = request.GET.get('status', None)
    tx_ref = request.GET.get('tx_ref', None)
    print(status)
    print(tx_ref)
    return HttpResponse('Finished')


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'home/about.html')
    
class ContactUsView(View):
    def get(self, request):
        return render(request, 'home/contact.html')
    
class AllContestantsView(View):
    def get(self, request):
        contestants = ContestantForm.objects.all()
        context = {
            'all_contestants':contestants,
        }
        return render(request, 'home/contestants/all-contestants.html', context)

class ContestantView(View):
    def get(self, request, pk):
        data = ContestantForm.objects.get(id=pk)
        form = PaymentForm()
        context = {
            'contestant':data,
            'form':form
        }
        return render(request, 'home/contestants/contestant-detail.html', context)

    def post(self, request, pk):
        data = ContestantForm.objects.get(id=pk)
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            amount = form.cleaned_data['amount']
            phone = form.cleaned_data['phone']
            return redirect(str(process_payment(name,email,amount,phone)))