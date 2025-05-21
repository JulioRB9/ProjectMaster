from django.contrib import admin
from .models import Categoria, Post # esta importacion viene desde el el modulo de views.py 

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

# Registra el modelo en el panel de adminstracion.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, BlogAdmin)
