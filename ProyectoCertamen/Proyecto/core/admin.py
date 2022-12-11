from django.contrib import admin

from core.models import Residencia
from core.models import Equipo

# Register your models here.

@admin.register(Residencia)
class AdminResidencia(admin.ModelAdmin):
    list_display = ('departamento',)
    ordering = ('-ID',)
    search_fields = ('ID',)

#admin.site.register(Residencia, AdminResidencia)


@admin.register(Equipo)
class RegistrarEquipo(admin.ModelAdmin):
    #list_display = ('destinatario','remitente','estado', 'conserje')
    ordering = ('-modelo',)
    #search_fields = ('destinatario',)
    #list_editable = ('estado', 'conserje')
    #list_filter = ('estado',)
    #list_per_page = 10
#admin.site.register(Equipo, RegistrarEquipo)

