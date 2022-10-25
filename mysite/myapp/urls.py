from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path('cines' , views.cine, name='main_cines'),
    path('cine/<int:id_cine>' , views.cine, name='details_cine'),

    path('salas' , views.cine, name='main_salas'),
    path('salas/<int:id_sala>' , views.cine, name='details_sala'),

    path('peliculas' , views.cine, name='main_peliculas'),
    path('peliculas/<int:id_pelicula>' , views.cine, name='details_pelicula'),
    path('peliculas/<int:id_pelicula>/director' , views.cine, name='details_director'),
    path('peliculas/<int:id_pelicula>/<int:id_actor>' , views.cine, name='details_actor')
]