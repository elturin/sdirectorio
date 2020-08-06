from django.db import models

# Create your models here.

class Entidad(models.Model):
    ruc    = models.CharField(max_length=11)
    nombre = models.CharField(max_length=400)
    sigla = models.CharField(max_length=6)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.sigla