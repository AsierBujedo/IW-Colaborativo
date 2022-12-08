from contextlib import nullcontext
from . import views 
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import *
from django.shortcuts import render
import random

class ViewIndex(ListView):
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

class ViewCines(ListView):
    model = Cine
    template_name = 'cines.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cines = Cine.objects.all()
    
        lista = []
        for cine in cines:
            salas_in_cine = cine.salas.all()
            peliculas_in_salas_in_cine = []
            for sala in salas_in_cine:
                for pelicula in sala.peliculas.all():
                    peliculas_in_salas_in_cine.append(pelicula)
            i = random.randint(0, len(peliculas_in_salas_in_cine) - 1)
            tupla = (cine, peliculas_in_salas_in_cine[i])
            lista.append(tupla)
            
        context['cine_list'] = lista

        return context

class ViewCine(DetailView):
    model = Cine
    template_name = 'cine.html'
    context_object_name = 'cine'

class ViewSalas(ListView):
    model = Sala
    template_name = 'salas.html'
    context_object_name = 'sala_list'

class ViewSala(DetailView):
    model = Sala
    template_name = 'sala.html'
    context_object_name = 'sala'

class ViewPeliculas(ListView):
    model = Pelicula
    template_name = 'peliculas.html'
    context_object_name = 'pelicula_list'

class ViewPelicula(DetailView):
    model = Pelicula
    template_name = 'pelicula.html'
    context_object_name = 'pelicula'

class ViewDirector(DetailView):
    model = Director
    template_name = 'director.html'
    context_object_name = 'director'

class ViewActor(DetailView):
    model = Actor
    template_name = 'actor.html'
    context_object_name = 'actor'