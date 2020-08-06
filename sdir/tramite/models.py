from django.db import models

# Create your models here.

class Tramite(models.Model):
    cut    = models.CharField(max_length=12)
    ruc = models.CharField(max_length=11)
    paso=models.IntegerField(default=0)
    accion = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.accion

class Cut(models.Model):
    cut    = models.CharField(max_length=12)
    ruc = models.CharField(max_length=11)
    codtramite = models.CharField(max_length=12)
    numero = models.IntegerField(default=0)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.cut