from contextlib import nullcontext
from . import views
from models import *
from django.shortcuts import render

# Create your views here.

def index(request):
    cines = Cine.objects.order_by('nombre')

    context = {
        'cines': cines
    }

    return render(request, 'index.html', context)

def cine(request):
    
    return 0

def sala(request):
    
    return 0

def pelicula(request):
    
    return 0

def actor(request):
    
    return 0