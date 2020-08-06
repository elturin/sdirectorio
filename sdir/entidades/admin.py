from django.contrib import admin
from .models import Entidad
# Register your models here.

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'sigla')
    search_fields = ('nombre',)