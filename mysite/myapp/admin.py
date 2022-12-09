from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from .models import Cine, Sala, Director, Pelicula, Actor 

admin.site.unregister(User)
admin.site.unregister(Group)

User.objects.get_or_create(username = 'user2', is_staff = True) 
u = User.objects.get(username = 'user2')
u.set_password('iw123456')
permission1 = Permission.objects.get(name='Can view user')
permission2 = Permission.objects.get(name='Can view actor')
permission3 = Permission.objects.get(name='Can view cine')
permission4 = Permission.objects.get(name='Can view director')
permission5 = Permission.objects.get(name='Can view pelicula')
permission6 = Permission.objects.get(name='Can view sala')
u.user_permissions.add(permission1, permission2, permission3, permission4, permission5, permission6)
u.save()

class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True
        return form

class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('inventory.change_product'):
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

class SalaInline(admin.TabularInline):
    model = Sala
    extra = 0

class CineAdmin(admin.ModelAdmin):
    fields = ['nombre', 'direccion', 'telefono', 'num_salas']
    list_display = ('nombre', 'direccion', 'telefono', 'num_salas')
    inlines = [SalaInline]

class PeliculaInline(admin.TabularInline):
    model = Pelicula
    extra = 0

class DirectorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_nto']
    list_display = ('nombre', 'fecha_nto')
    list_filter = ['fecha_nto']
    search_fields = ['nombre']
    search_help_text = 'Filtrar por nombre'
    inlines = [PeliculaInline]

class ActorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_nto']
    list_display = ('nombre', 'fecha_nto')
    list_filter = ['fecha_nto']
    search_fields = ['nombre']
    search_help_text = 'Filtrar por nombre'

class SalaAdmin(admin.ModelAdmin):
    fields = ['cod_sala', 'num_asientos', 'categoria', 'id_cine']
    list_display = ('cod_sala', 'num_asientos', 'categoria', 'id_cine')

class PeliculaAdmin(admin.ModelAdmin):
    fields = ['actores', 'salas', 'titulo', 'fecha_estreno', 'longitud_mins', 'id_director']
    list_display = ('titulo', 'fecha_estreno', 'longitud_mins', 'id_director')
    list_filter = ['fecha_estreno']
    search_fields = ['titulo']
    search_help_text = 'Filtrar por título'

admin.site.register(User, UserAdmin)
admin.site.register(Cine, CineAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Pelicula, PeliculaAdmin)