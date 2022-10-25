from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('/cine' , views.cine, name='cine'),
    path('/cine/sala' , views.cine, name='salas'),
    path('/cine/sala/pelicula' , views.cine, name='peliculas'),
    path('/cine/sala/pelicula/actor' , views.cine, name='actores'),
    path('/cine/sala/pelicula/director' , views.cine, name='director')
]