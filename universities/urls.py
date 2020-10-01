from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('universities/', views.universities, name='universities'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
