from . import views
from django.urls import path

urlpatterns = [
    #localhost:8000/myapp/
    path('', views.ViewIndex.as_view(), name='index'),
    #path('', views.index, name='index'),

    #localhost:8000/myapp/cines
    path('cines', views.ViewCines.as_view(), name='main_cines'),
    #localhost:8000/myapp/cines/<int:id_cine>
    path('cines/<int:pk>', views.ViewCine.as_view(), name='details_cine'),

    #localhost:8000/myapp/salas
    path('salas', views.ViewSalas.as_view(), name='main_salas'),
    #path('salas', views.salas, name='main_salas'),
    #localhost:8000/myapp/salas/<int:id_sala>
    path('salas/<int:pk>', views.ViewSala.as_view(), name='details_sala'),

    #localhost:8000/myapp/peliculas
    path('peliculas', views.ViewPeliculas.as_view(), name='main_peliculas'),
    #localhost:8000/myapp/peliculas/<int:id_pelicula>
    path('peliculas/<int:pk>', views.ViewPelicula.as_view(), name='details_pelicula'),
    #localhost:8000/myapp/directores/<int:id_director>
    path('directores/<int:pk>', views.ViewDirector.as_view(), name='details_director'),
    #localhost:8000/myapp/actores/<int:id_actor>
    path('actores/<int:pk>', views.ViewActor.as_view(), name='details_actor')
]