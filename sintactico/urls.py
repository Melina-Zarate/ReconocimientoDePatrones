from django.urls import path
from .views import sintactico

app_name = ''

urlpatterns = [
    path("sintactico/", sintactico, name="sintactico")
]