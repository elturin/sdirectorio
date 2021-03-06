from django.db import models

# Create your models here.
class Indicador(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre