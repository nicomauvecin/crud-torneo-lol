from django.forms import ModelForm

from equipos_jugadores.models import Equipo, Jugador


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'


class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
