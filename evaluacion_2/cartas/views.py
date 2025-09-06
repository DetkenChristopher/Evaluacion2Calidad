from django.shortcuts import render
from cartas.models import Carta

def lista_cartas(request):
    cartas = Carta.objects.all()
    return render(request, 'Carta/lista_cartas.html', {'cartas': cartas})

def detalle_carta(request, id):
    carta = Carta.objects.get(id=id)
    return render(request, 'Carta/detalle_carta.html', {'carta': carta})
