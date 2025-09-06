from django.urls import path
from .views import *
from cartas import views

urlpatterns = [
     path('', lista_cartas, name='lista_cartas'),
    path('carta/<int:id>/',detalle_carta, name='detalle_carta'),
   
    
]