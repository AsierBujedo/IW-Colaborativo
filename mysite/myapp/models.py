from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Cine(models.Model):
    id_cine = models.IntegerField().primary_key
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    num_salas = models.IntegerField()
    
class Sala(models.Model):
    id_sala = models.IntegerField().primary_key
    num_sala = models.IntegerField()
    num_asientos = models.IntegerField()
    categoria = models.CharField(max_length=50)
    id_cine = models.ForeignKey(Cine, on_delete=models.CASCADE)
    
class Director(models.Model):
    id_director = models.IntegerField().primary_key
    nombre = models.CharField(max_length=50)
    fecha_nto = models.DateField()

class Pelicula(models.Model):
    id_pelicula = models.IntegerField().primary_key
    titulo = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    longitud_mins = models.FloatField()
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    id_director = models.ForeignKey(Director, on_delete=models.CASCADE)
      
class Actor(models.Model):
    id_actor = models.IntegerField().primary_key
    peliculas = models.ManyToManyField(Pelicula) # Nos lo tiene que confirmar Asier
    nombre = models.CharField(max_length=50)
    fecha_nto = models.DateField()

# Valor por defecto (default = 0)