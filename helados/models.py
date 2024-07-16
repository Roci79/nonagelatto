from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class HeladoRecipienteCristal(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(null=True, blank=True,upload_to='images/')

    def __str__(self):
         return f"{self.nombre} - Recipiente de Cristal"

class Sabor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(null=True, blank=True,upload_to='images/')
   
    def __str__(self):
        return f"{self.nombre}"


    


    