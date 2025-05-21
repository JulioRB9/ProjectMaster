from django.urls import path
from . import views
from django.conf.urls.static import static

# https://www.youtube.com/watch?v=Dsgsfnp8RA8&t=182s
urlpatterns = [
    path('',views.blog,name='blog'),
    path('categoria/<int:categoria_id>/',views.categoria,name='categoria'),
] 