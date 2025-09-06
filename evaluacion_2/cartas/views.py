from django.shortcuts import render, get_object_or_404
from cartas.models import Carta

def lista_cartas(request):
    cartas = Carta.objects.all()
    return render(request, 'cartas/lista_cartas.html', {'cartas': cartas})

def detalle_carta(request, carta_id):
    carta = get_object_or_404(Carta, pk=carta_id)
    return render(request, 'cartas/detalle_carta.html', {'carta': carta})
