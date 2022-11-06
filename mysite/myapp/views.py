from contextlib import nullcontext
from . import views
from .models import *
from django.shortcuts import render

# Create your views here.

def index(request):
    cines = Cine.objects.all()


    context = {
        'cines': cines
    }

    return render(request, 'index.html', context)

def cines(request):
    cines = Cine.objects.all()

    context = {
        'cines': cines
    }

    return render(request, 'cines.html', context)

def cine(request, id_cine):
    cine = Cine.objects.get(pk=id_cine)
    salas = Sala.objects.filter(id_cine, id_cine)

    context = {
        'cine': cine,
        'salas': salas
    }

    return render(request, 'cine.html', context)

def salas(request):
    salas = Sala.objects.all()

    context = {
        'salas': salas
    }

    return render(request, 'salas.html', context)

def sala(request, id_sala):
    sala = Sala.objects.get(pk=id_sala)

    context = {
        'sala': sala
    }

    return render(request, 'sala.html', context)

def peliculas(request):
    peliculas = Pelicula.objects.all()

    context = {
        'peliculas': peliculas
    }

    return render(request, 'peliculas.html', context)

def pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(pk=id_pelicula)
    #director =
    #actores =

    context = {
        'pelicula': pelicula
        #'director': director
        #'actores': actores
    }

    return render(request, 'pelicula.html', context)

def director(request):
    
    return 0

def actor(request):
    
    return 0