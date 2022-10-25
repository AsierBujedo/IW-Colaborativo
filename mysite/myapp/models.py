from django.db import models


# Create your models here.
class Cine(models.Model):
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    telefono= models.CharField(max_length=50)
    num_salas= models.IntegerField()
class Sala(models.Model):
    num_asientos = models.IntegerField()
    categoria = models.CharField(max_length=50)
    id_cine = models.ForeignKey(Cine, on_delete=models.)
class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    Longitud_mins = models.FloatField()
class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nto = models.DateField()