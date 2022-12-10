from django.contrib import admin

from core.models import Residencia
from core.models import Correspondencia

# Register your models here.

@admin.register(Residencia)
class AdminResidencia(admin.ModelAdmin):
    list_display = ('ID','dueño', 'telefono')
    ordering = ('-ID',)
    search_fields = ('ID',)

#admin.site.register(Residencia, AdminResidencia)


@admin.register(Correspondencia)
class RegistrarCorrespondencia(admin.ModelAdmin):
    list_display = ('destinatario','remitente','estado', 'conserje')
    ordering = ('-destinatario',)
    search_fields = ('destinatario',)
    list_editable = ('estado', 'conserje')
    list_filter = ('estado',)
    list_per_page = 10
#admin.site.register(Correspondencia, RegistrarCorrespondencia)

