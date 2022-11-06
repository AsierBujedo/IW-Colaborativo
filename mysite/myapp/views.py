from contextlib import nullcontext
from . import views
from .models import *
from django.shortcuts import render
import random

# Create your views here.

def index(request):
    cines = Cine.objects.all()
    #cine1 = Cine.objects.get(pk = 1)
    #cine2 = Cine.objects.get(pk = 2)
    #cine3 = Cine.objects.get(pk = 3)
    #cine4 = Cine.objects.get(pk = 4)
    salas = []
    salas_in_cine1 = Sala.objects.filter(id_cine = cines[0]).order_by('-num_asientos')
    salas_in_cine2 = Sala.objects.filter(id_cine = cines[1]).order_by('-num_asientos')
    salas_in_cine3 = Sala.objects.filter(id_cine = cines[2]).order_by('-num_asientos')
    salas_in_cine4 = Sala.objects.filter(id_cine = cines[3]).order_by('-num_asientos')
    salas.append(salas_in_cine1[0])
    salas.append(salas_in_cine2[0])
    salas.append(salas_in_cine3[0])
    salas.append(salas_in_cine4[0])
    #salas_in_cine1 = Sala.objects.filter(id_cine = cine_1).order_by('-num_asientos')
    #salas_in_cine2 = Sala.objects.filter(id_cine = cine_2).order_by('-num_asientos')
    #salas_in_cine3 = Sala.objects.filter(id_cine = cine_3).order_by('-num_asientos')
    #salas_in_cine4 = Sala.objects.filter(id_cine = cine_4).order_by('-num_asientos')
    #sala_num_max_asientos_in_cine1 = salas_in_cine_1[0]
    #sala_num_max_asientos_in_cine2 = salas_in_cine_2[0]
    #sala_num_max_asientos_in_cine3 = salas_in_cine_3[0]
    #sala_num_max_asientos_in_cine4 = salas_in_cine_4[0]

    context = {
        'cines': cines,
        'salas': salas
        #'cine1': cine_1,
        #'cine2': cine_2,
        #'cine3': cine_3,
        #'cine4': cine_4,
        #'sala_num_max_asientos_in_cine1': sala_num_max_asientos_in_cine1,
        #'sala_num_max_asientos_in_cine2': sala_num_max_asientos_in_cine2,
        #'sala_num_max_asientos_in_cine3': sala_num_max_asientos_in_cine3,
        #'sala_num_max_asientos_in_cine4': sala_num_max_asientos_in_cine4
    }

    return render(request, 'index.html', context)

def cines(request):
    cines = Cine.objects.all()

    context = {
        'cines': cines,
    }

    return render(request, 'cines.html', context)

def cine(request, id_cine):
    cine = Cine.objects.get(pk=id_cine)
    salas = Sala.objects.filter(id_cine = id_cine)

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
    #peliculas = Pelicula.objects.filter(id_sala = id_sala)
    peliculas_in_sala = Pelicula.objects.filter(salas__in = [id_sala])

    context = {
        'sala': sala,
        'peliculas_in_sala': peliculas_in_sala
    }

    return render(request, 'sala.html', context)

def peliculas(request):
    peliculas = Pelicula.objects.all()

    context = {
        'peliculas': peliculas
    }

    return render(request, 'peliculas.html', context)

def pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(pk = id_pelicula)
    actores_in_pelicula = Actor.objects.filter(pelicula__in = [id_pelicula])
    #cine_contains_sala_projects_pelicula = Cine.objects.get(pk = Sala.objects.get(pk = Pelicula.objects.get(pk = id_pelicula).id_sala.id).id_cine.id)
    salas_in_pelicula = Sala.objects.filter(pelicula__in = [id_pelicula])
    
    cines = []
    for sala in salas_in_pelicula:
        cine = Cine.objects.get(pk = sala.id_cine.id)
        if cine not in cines:
            cines.append(cine)

    context = {
        'pelicula': pelicula,
        'actores_in_pelicula': actores_in_pelicula,
        #'cine_contains_sala_projects_pelicula': cine_contains_sala_projects_pelicula
        'cines': cines
    }

    return render(request, 'pelicula.html', context)

def director(request, id_director):
    director = Director.objects.get(pk=id_director)

    context = {
        'director': director
    }

    return render(request, 'director.html', context)

def actor(request, id_actor):
    actor = Actor.objects.get(pk=id_actor)

    context = {
        'actor': actor
    }

    return render(request, 'actor.html', context)