from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    
class AboutUsView(View):
    def get(self, request):
        return render(request, 'home/about.html')
    
class ContactUsView(View):
    def get(self, request):
        return render(request, 'home/contact.html')

class ContestantView(View):
    def get(self, request):
        return render(request, 'home/contestant.html')
    