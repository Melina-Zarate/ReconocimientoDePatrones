from django.urls import path
from .views import home, noHome, nueva

app_name = 'home' #Nombre a las vistas

urlpatterns = [
    path('', home, name = 'home' ),  #nombre de la app a ingresar en la url, nombreAReferir de la url
    path('noHome/', noHome, name = 'noHome' ), 
    path('nueva/', nueva, name = 'nueva' ), 
]
