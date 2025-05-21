from django.shortcuts import render, HttpResponse
from servicios.models import servicio

# Create your views here.
def home(request):
    return render(request, "appFrontend/home.html")

def tienda(request):
    return render(request, "appFrontend/tienda.html")

def contacto(request):
    return render(request, "appFrontend/contacto.html")
