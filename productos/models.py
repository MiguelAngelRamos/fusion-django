from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    image = models.URLField(verbose_name="URL de la imagen")
    precio = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre