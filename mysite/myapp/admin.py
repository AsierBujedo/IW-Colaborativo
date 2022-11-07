from django.contrib import admin
from .models import Cine, Sala, Director, Pelicula, Actor 

admin.site.register(Cine)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Sala)
admin.site.register(Pelicula)