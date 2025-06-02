from django.urls import path
from . import views

# https://www.youtube.com/watch?v=C8cn-Z-Ps4A&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB&index=43
urlpatterns = [
    path('',views.tienda,name='tienda'),
] 