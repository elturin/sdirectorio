from django.contrib import admin
from .models import Indicador
# Register your models here.

@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)