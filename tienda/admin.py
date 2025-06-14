from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

# Registra el modelo en el panel de adminstracion.
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)


