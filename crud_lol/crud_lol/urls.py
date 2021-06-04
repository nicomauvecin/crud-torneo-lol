"""crud_lol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from equipos_jugadores.views import detalle_equipo, editar_equipo, borrar_equipo, agregar_equipo, jugadores, agregar_jugador, \
    detalle_jugador, editar_jugador, borrar_jugador
from webapp.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('detalle_equipo/<int:id>', detalle_equipo),
    path('editar_equipo/<int:id>', editar_equipo),
    path('borrar_equipo/<int:id>', borrar_equipo),
    path('agregar_equipo/', agregar_equipo, name='agregar-equipo'),
    path('jugadores/', jugadores, name='jugadores'),
    path('agregar_jugador/', agregar_jugador, name='agregar-jugador'),
    path('detalle_jugador/<int:id>', detalle_jugador),
    path('editar_jugador/<int:id>', editar_jugador),
    path('borrar_jugador/<int:id>', borrar_jugador)
]
