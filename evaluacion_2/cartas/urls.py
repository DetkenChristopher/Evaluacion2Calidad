from django.urls import path
from .views import *
from cartas import views

urlpatterns = [
     path('', views.lista_cartas, name='lista_cartas'),
    path('carta/<int:carta_id>/', views.detalle_carta, name='detalle_carta'),
   
    
]