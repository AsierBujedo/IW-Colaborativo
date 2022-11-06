from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path('cines' , views.cines, name='main_cines'),
    path('cines/<int:id_cine>' , views.cine, name='details_cine'),

    path('salas' , views.salas, name='main_salas'),
    path('salas/<int:id_sala>' , views.sala, name='details_sala'),

    path('peliculas' , views.peliculas, name='main_peliculas'),
    path('peliculas/<int:id_pelicula>' , views.pelicula, name='details_pelicula'),
    path('peliculas/<int:id_pelicula>/director' , views.director, name='details_director'),
    path('peliculas/<int:id_pelicula>/<int:id_actor>' , views.actor, name='details_actor')
]