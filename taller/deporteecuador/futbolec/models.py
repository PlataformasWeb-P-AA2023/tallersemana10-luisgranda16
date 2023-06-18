from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField('Nombre del equipo', max_length=40)
    siglas = models.CharField(max_length=30)
    twitter = models.CharField('Usuario de Twitter', max_length=30)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipos')

    def __str__(self):
        return "Nombre: %s - Siglas: %s - Twitter: %s" % (self.nombre, self.siglas, self.twitter)


class Jugadores(models.Model):
    nombre = models.CharField('Nombre Jugador', max_length=40)
    posicion = models.CharField(max_length=50)
    numero = models.IntegerField('Numero de camiseta')
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return "Nombre: %s - Posición: %s - Camiseta: %s - Sueldo: %s" % (self.nombre, self.posicion, self.numero, self.sueldo)


class Campeonato(models.Model):
    nombre = models.CharField('Nombre del campeonato', max_length=50)
    auspiciante = models.CharField('Nombre del auspiciante', max_length=50)
    equipos = models.ManyToManyField(EquipoFutbol, through='CampeonatoEquipos')

    def __str__(self):
        return "Nombre: %s - Auspiciante: %s" % (self.nombre, self.auspiciante)


class CampeonatoEquipos(models.Model):
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    anio = models.IntegerField()

    def __str__(self):
        return "Equipo: %s - Campeonato: %s - Año: %s" % (self.equipo, self.campeonato, self.anio)