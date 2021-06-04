from django.contrib import admin

# Register your models here.
from equipos_jugadores.models import Jugador, Equipo, Jugador_Equipo, Posicion

admin.site.register(Posicion)
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Jugador_Equipo)
