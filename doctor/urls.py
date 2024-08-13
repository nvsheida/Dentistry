from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('dentist/', views.dentists_view, name='dentist'),
    path('contact/', views.contact_view, name='contact'),
    path('booking/', views.booking_view, name='booking'),
]
