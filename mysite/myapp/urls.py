from . import views
from django.urls import path

urlpatterns = [
    #localhost:8000/myapp/
    path('', views.Index.as_view(), name='index'),
    #path('', views.index, name='index'),

    #localhost:8000/myapp/cines
    path('cines', views.Cines.as_view(), name='main_cines'),
    #localhost:8000/myapp/cines/<int:id_cine>
    path('cines/<int:id_cine>', views.cine, name='details_cine'),

    #localhost:8000/myapp/salas
    path('salas', views.Salas.as_view(), name='main_salas'),
    #path('salas', views.salas, name='main_salas'),
    #localhost:8000/myapp/salas/<int:id_sala>
    path('salas/<int:id_sala>', views.sala, name='details_sala'),

    #localhost:8000/myapp/peliculas
    path('peliculas', views.Peliculas.as_view(), name='main_peliculas'),
    #localhost:8000/myapp/peliculas/<int:id_pelicula>
    path('peliculas/<int:id_pelicula>', views.pelicula, name='details_pelicula'),
    #localhost:8000/myapp/directores/<int:id_director>
    path('directores/<int:id_director>', views.director, name='details_director'),
    #localhost:8000/myapp/actores/<int:id_actor>
    path('actores/<int:id_actor>', views.actor, name='details_actor')
]