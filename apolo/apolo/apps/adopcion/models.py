from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Persona(AbstractUser):
    activos = models.CharField(blank=True, max_length=100)
    numeroEmpl = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(blank=True, max_length=100)
    
