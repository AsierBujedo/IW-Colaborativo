from unittest.util import _MAX_LENGTH
from django.db import models

class Cine(models.Model):
    nombre = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    num_salas = models.IntegerField()

class Director(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_nto = models.DateField()

class Actor(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_nto = models.DateField()

class Sala(models.Model):
    cod_sala = models.CharField(max_length = 50)
    num_asientos = models.IntegerField()
    categoria = models.CharField(max_length = 50)
    id_cine = models.ForeignKey(Cine, on_delete = models.CASCADE, related_name = 'salas')

class Pelicula(models.Model):
    actores = models.ManyToManyField(Actor, related_name = 'peliculas')
    salas = models.ManyToManyField(Sala, related_name = 'peliculas')
    titulo = models.CharField(max_length = 50)
    fecha_estreno = models.DateField()
    longitud_mins = models.IntegerField()
    id_director = models.ForeignKey(Director, on_delete = models.CASCADE, related_name = 'peliculas')