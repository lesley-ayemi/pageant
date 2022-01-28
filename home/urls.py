from django.urls import path
from .views import AboutUsView, AllContestantsView, CancelView, ContactUsView, CreateCheckoutSessionView, GalleryView, HomeView, ContestantView, RegisterView, SuccessView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('apply/', RegisterView.as_view(), name='register'),
    path('contestant/<pk>/', ContestantView.as_view(), name='contestant'),
    path('all-contestants/', AllContestantsView.as_view(), name='all-contestants'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    # path('checkout/', checkout, name='checkout'),
]
