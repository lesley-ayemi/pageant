from django.urls import path
from .views import AboutUsView, AllContestantsView, ContactUsView, HomeView, ContestantView, payment_response

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('contestant/<str:pk>/', ContestantView.as_view(), name='contestant'),
    path('all-contestants/', AllContestantsView.as_view(), name='all-contestants'),
    path('callback', payment_response, name='payment_response'),
]
