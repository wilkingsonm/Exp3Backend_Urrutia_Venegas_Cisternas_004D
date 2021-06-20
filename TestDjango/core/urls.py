from django.urls import path
from .views import home,index,galeria,registro

urlpatterns = [

    path('home', home, name="home"),
    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('registro', registro, name="registro"),
]