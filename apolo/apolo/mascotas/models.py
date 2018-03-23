from django.db import models

# Create your models here.

class Mascota(models.Model):
    folio = models.CharField(blank=True, max_length=100, primary_key=True)
    nombre = models.CharField(blank=True, max_length=100)
    sexo = models.CharField(blank=True, max_length=100)
    edad = models.IntegerField(blank=True, null=True)
    fecha_RESCATE = models.DateField(default=datetime.datetime.today)
