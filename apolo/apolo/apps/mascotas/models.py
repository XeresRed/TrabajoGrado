from django.db import models
from apps.adopcion.models import Persona
import datetime

# Create your models here.

class Vacuna(models.Model):
    Nombre = models.CharField(blank=True, max_length=100)
    def __str__(self):
        return "{}".format(self.Nombre)

class Mascota(models.Model):
    nombre = models.CharField(blank=True, max_length=100)
    sexo = models.CharField(blank=True, max_length=100)
    edad = models.IntegerField(blank=True, null=True)
    fecha_RESCATE = models.DateField(default=datetime.datetime.today)
    persona = models.ForeignKey(Persona,null = True, blank=True,on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna)

    def __str__(self):
        return "{}".format(self.nombre)
