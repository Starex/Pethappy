from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_mascota = models.CharField(max_length=100, default="Sin nombre")
    peso = models.FloatField()
    raza = models.CharField(max_length=100)
    comida = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre