from unittest.util import _MAX_LENGTH
from django.db import models

class Cine(models.Model):
    nombre = models.CharField(max_length = 50)
    direccion = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    num_salas = models.IntegerField()

    def __str__(self):
         return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_nto = models.DateField()

    class Meta:
      verbose_name_plural = "Directores"

    def __str__(self):
         return self.nombre

class Actor(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_nto = models.DateField()

    class Meta:
      verbose_name_plural = "Actores"

    def __str__(self):
         return self.nombre

class Sala(models.Model):
    cod_sala = models.CharField(max_length = 50)
    num_asientos = models.IntegerField()
    categoria = models.CharField(max_length = 50)
    id_cine = models.ForeignKey(Cine, on_delete = models.CASCADE, related_name = 'salas')

    def __str__(self):
         return self.cod_sala

class Pelicula(models.Model):
    actores = models.ManyToManyField(Actor, related_name = 'peliculas')
    salas = models.ManyToManyField(Sala, related_name = 'peliculas')
    titulo = models.CharField(max_length = 50)
    fecha_estreno = models.DateField()
    longitud_mins = models.IntegerField()
    id_director = models.ForeignKey(Director, on_delete = models.CASCADE, related_name = 'peliculas')

    def __str__(self):
         return self.titulo