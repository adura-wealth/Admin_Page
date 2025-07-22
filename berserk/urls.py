from django.urls import path
from . import views

urlpatterns = [
    path('', views.disc),
    path('contact/', views.contact),
]
