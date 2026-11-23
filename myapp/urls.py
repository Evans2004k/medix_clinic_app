# myapp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('departments/details/', views.department_details, name='department_details'),
    path('services/', views.services, name='services'),
    path('services/details/', views.service_details, name='service_details'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('starter/', views.starter, name='starter'),
    path('404/', views.not_found, name='not_found'),
]