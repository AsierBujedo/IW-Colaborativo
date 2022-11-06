from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Cine(models.Model):
    #id_cine = models.IntegerField().primary_key
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    num_salas = models.IntegerField()

class Director(models.Model):
    #id_director = models.IntegerField().primary_key
    nombre = models.CharField(max_length=50)
    fecha_nto = models.DateField()

class Actor(models.Model):
    #id_actor = models.IntegerField().primary_key
    nombre = models.CharField(max_length=50)
    fecha_nto = models.DateField()

class Sala(models.Model):
    #id_sala = models.IntegerField().primary_key
    cod_sala = models.CharField(max_length=50)
    num_asientos = models.IntegerField()
    categoria = models.CharField(max_length=50)
    id_cine = models.ForeignKey(Cine, on_delete=models.CASCADE)

class Pelicula(models.Model):
    #id_pelicula = models.IntegerField().primary_key
    actores = models.ManyToManyField(Actor)
    salas = models.ManyToManyField(Sala)
    titulo = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    longitud_mins = models.IntegerField()
    id_director = models.ForeignKey(Director, on_delete=models.CASCADE)