from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from equipos_jugadores.forms import EquipoForm, JugadorForm
from equipos_jugadores.models import Equipo, Jugador


def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    return render(request, 'equipos/detalle.html', {'equipo': equipo})


def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    if request.method == 'POST':
        formaEquipo = EquipoForm(request.POST, instance=equipo)
        if formaEquipo.is_valid():
            formaEquipo.save()
            return redirect('index')
    else:
        formaEquipo = EquipoForm(instance=equipo)
    return render(request, 'equipos/editar.html', {'formaEquipo': formaEquipo})


def borrar_equipo(request, id):
    equipo = get_object_or_404(Equipo, pk=id)
    if equipo:
        equipo.delete()
    return redirect('index')


def agregar_equipo(request):
    if request.method == 'POST':
        formaEquipo = EquipoForm(request.POST)
        if formaEquipo.is_valid():
            formaEquipo.save()
            return redirect('index')
    else:
        formaEquipo = EquipoForm()
    return render(request, 'equipos/agregar.html', {'formaEquipo': formaEquipo})


def jugadores(request):
    jugadores = Jugador.objects.order_by('usuario')
    return render(request, 'jugadores/jugadores.html', {'jugadores': jugadores})


def agregar_jugador(request):
    if request.method == 'POST':
        formaJugador = JugadorForm(request.POST)
        if formaJugador.is_valid():
            formaJugador.save()
            return redirect('jugadores')
    else:
        formaJugador = JugadorForm()
    return render(request, 'jugadores/agregar.html', {'formaJugador': formaJugador})

def detalle_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    return render(request, 'jugadores/detalle.html', {'jugador': jugador})


def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    if request.method == 'POST':
        formaJugador = JugadorForm(request.POST, instance=jugador)
        if formaJugador.is_valid():
            formaJugador.save()
            return redirect('index')
    else:
        formaJugador = JugadorForm(instance=jugador)
    return render(request, 'jugadores/editar.html', {'formaJugador': formaJugador})


def borrar_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    if jugador:
        jugador.delete()
    return redirect('jugadores')
