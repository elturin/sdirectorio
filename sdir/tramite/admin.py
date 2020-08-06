from django.contrib import admin
from .models import Tramite, Cut
# Register your models here.

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    list_display = ('cut', 'ruc', 'paso', 'accion')
    search_fields = ('cut',)


@admin.register(Cut)
class CutAdmin(admin.ModelAdmin):
    list_display = ('id', 'cut', 'ruc', 'codtramite', 'numero')
    search_fields = ('cut',)