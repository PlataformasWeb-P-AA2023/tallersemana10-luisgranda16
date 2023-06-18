from django.contrib import admin

# Register your models here.
from futbolec.models import EquipoFutbol, Jugadores, Campeonato, CampeonatoEquipos

class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')
    search_fields = ('nombre', 'siglas')

admin.site.register(EquipoFutbol, EquipoFutbolAdmin)

class JugadoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numero', 'sueldo', 'equipo')
    search_fields = ('nombre', 'numero')

admin.site.register(Jugadores, JugadoresAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'auspiciante')
    search_fields = ('nombre',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEquiposAdmin(admin.ModelAdmin):
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo', 'campeonato')

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)