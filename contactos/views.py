from django.shortcuts import render
from .forms import formularioContacto

# Create your views here.
def contacto(request):
    formulario = formularioContacto()
    return render(request, "contactos/contacto.html", {"miformulario": formulario})