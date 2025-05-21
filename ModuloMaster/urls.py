"""
URL configuration for ModuloMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Jerarquia de carpetas en el proyecto 
# ModuloMaster      : Raiz del proyecto va estar linchada todas la aplicaciones que estemos agregando 
# appFrontend   : Aplicacion Principal
# blogs     : Aplicacion de Blogs
# contactos : Aplicacion de Contactos
# servicios : Aplicacion de Servicios

from django.contrib import admin
from django.urls import path, include
# Minuto 7.19
# https://www.youtube.com/watch?v=PRdrrxCggIU&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=36
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')), # Aplicacion de Servicios
    path('blogs/', include('blogs.urls')),  # Aplicacion de Blogs
    path('contactos/', include('contactos.urls')), # Aplicacion de Contactos
    path('', include('appFrontend.urls')),    # Aplicacion Principal 
]
