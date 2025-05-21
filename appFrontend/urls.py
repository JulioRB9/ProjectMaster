from django.urls import path
from appFrontend import views
from django.conf import settings
from django.conf.urls.static import static

# https://www.youtube.com/watch?v=Dsgsfnp8RA8&t=182s
urlpatterns = [
    path('',views.home,name='home'),
    path('tienda/',views.tienda,name='tienda'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
