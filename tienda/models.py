from django.db import models

# https://youtu.be/da3FIYSDMGQ?si=ZNZhswbHvOZkqVmP
# Create your models here.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categorias Productos'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(default='Producto sin descripción disponible')
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre
