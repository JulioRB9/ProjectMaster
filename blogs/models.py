from django.db import models
from django.contrib.auth.models import User

# https://www.youtube.com/watch?v=ClbbhYN8_ec&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=38   minuto 15:14 mm
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #puede eliminar todo los pos creado por el usuario
    categorias = models.ManyToManyField(Categoria)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo