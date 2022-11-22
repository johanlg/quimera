from django.db import models

# Create your models here.

class PlacaBase(models.Model):

    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)