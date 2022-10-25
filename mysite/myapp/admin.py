from django.contrib import admin
from .models import Cine, Sala, Director, Pelicula, Actor 

# Register your models here.

admin.site.register(Cine)
admin.site.register(Sala)
admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Actor)