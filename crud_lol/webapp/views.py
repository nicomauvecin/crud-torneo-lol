from django.shortcuts import render

# Create your views here.
from equipos_jugadores.models import Equipo


def inicio(request):
    equipos = Equipo.objects.order_by('-PG')
    return render(request, 'index.html', {'equipos': equipos})
