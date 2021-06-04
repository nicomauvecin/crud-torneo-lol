from django.db import models


# Create your models here.


class Posicion(models.Model):
    posicion = models.CharField(max_length=30)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.posicion}'


class Jugador(models.Model):
    usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    edad = models.IntegerField(blank=True, null=True)
    posicion = models.ForeignKey(Posicion, on_delete=models.SET_NULL, null=True)

    K = models.IntegerField(blank=True, null=True)
    D = models.IntegerField(blank=True, null=True)
    A = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.usuario}'


class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    jugador1 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, related_name='jug1')
    jugador2 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, related_name='jug2')
    jugador3 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, related_name='jug3')
    jugador4 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, related_name='jug4')
    jugador5 = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True, related_name='jug5')
    suplente = models.ForeignKey(Jugador, on_delete=models.SET_NULL, blank=True, null=True, related_name='suplente')

    PJ = models.IntegerField(blank=True, null=True)
    PG = models.IntegerField(blank=True, null=True)
    PP = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'[{self.id}] - {self.nombre} | W/L: {self.PG}/{self.PP}'


class Jugador_Equipo(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.SET_NULL, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
