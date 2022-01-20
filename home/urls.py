from django.urls import path
from .views import AboutUsView, BootView, ContactUsView, HomeView, ContestantView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('boot/', BootView.as_view(), name='boot'),
    path('contestant/', ContestantView.as_view(), name='contestant'),
]
