from contextlib import nullcontext
from . import views 
from django.views.generic import ListView
from .models import *
from django.shortcuts import render
import random

class Index(ListView):
    model = Cine
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cines = Cine.objects.all()

        lista = []
        for cine in cines:
            salas_in_cine = Sala.objects.filter(id_cine = cine).order_by('-num_asientos')
            tupla = (cine, salas_in_cine)
            lista.append(tupla)
            
        context['cine_list'] = lista

        return context

""" def index(request):
    cines = Cine.objects.all()

    lista = []
    for cine in cines:
        salas_in_cine = Sala.objects.filter(id_cine = cine).order_by('-num_asientos')
        tupla = (cine, salas_in_cine)
        lista.append(tupla)

    context = {
        'lista': lista
    }

    return render(request, 'index.html', context) """

class Cines(ListView):
    model = Cine
    template_name = 'cines.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cines = Cine.objects.all()
    
        lista = []
        for cine in cines:
            salas_in_cine = cine.id_cine.all()
            #salas_in_cine = Sala.objects.filter(id_cine = cine)
            peliculas_in_salas_in_cine = []
            for sala in salas_in_cine:
                for pelicula in sala.peliculas.all():
                    peliculas_in_salas_in_cine.append(pelicula)
            #peliculas_in_salas_in_cine = Pelicula.objects.filter(salas__in = salas_in_cine)
            i = random.randint(0, len(peliculas_in_salas_in_cine) - 1)
            tupla = (cine, peliculas_in_salas_in_cine[i])
            lista.append(tupla)
            
        context['cine_list'] = lista

        return context

""" def cines(request):
    cines = Cine.objects.all()
    
    lista = []
    for cine in cines:
        salas_in_cine = Sala.objects.filter(id_cine = cine)
        peliculas_in_salas_in_cine = Pelicula.objects.filter(salas__in = salas_in_cine)
        i = random.randint(0, len(peliculas_in_salas_in_cine) - 1)
        tupla = (cine, peliculas_in_salas_in_cine[i])
        lista.append(tupla)

    context = {
        'lista': lista,
    }

    return render(request, 'cines.html', context) """

def cine(request, id_cine):
    cine = Cine.objects.get(pk=id_cine)
    salas = Sala.objects.filter(id_cine = id_cine)

    context = {
        'cine': cine,
        'salas': salas
    }

    return render(request, 'cine.html', context)

class Salas(ListView):
    model = Sala
    context_object_name = 'sala_list'
    template_name = 'salas.html'

""" def salas(request):
    salas = Sala.objects.all()

    context = {
        'salas': salas
    }

    return render(request, 'salas.html', context) """

def sala(request, id_sala):
    sala = Sala.objects.get(pk=id_sala)
    peliculas_in_sala = sala.peliculas.all()
    #peliculas_in_sala = Pelicula.objects.filter(salas__in = [id_sala])

    context = {
        'sala': sala,
        'peliculas_in_sala': peliculas_in_sala
    }

    return render(request, 'sala.html', context)

class Peliculas(ListView):
    model = Pelicula
    context_object_name = 'pelicula_list'
    template_name = 'peliculas.html'

""" def peliculas(request):
    peliculas = Pelicula.objects.all()

    context = {
        'peliculas': peliculas
    }

    return render(request, 'peliculas.html', context) """

def pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(pk = id_pelicula)
    actores_in_pelicula = Actor.objects.filter(peliculas__in = [id_pelicula])
    salas_in_pelicula = Sala.objects.filter(peliculas__in = [id_pelicula])
    
    cines = []
    for sala in salas_in_pelicula:
        cine = Cine.objects.get(pk = sala.id_cine.id)
        if cine not in cines:
            cines.append(cine)

    context = {
        'pelicula': pelicula,
        'actores_in_pelicula': actores_in_pelicula,
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