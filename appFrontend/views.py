from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "appFrontend/home.html")

def tienda(request):
    return render(request, "appFrontend/tienda.html")
