from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tejido

def home(request):
    lista = Tejido.objects.get_queryset()
    #Procesamos la lista
    procesada = procesaLista(lista)
    template_name = "home/index.html"
    diccionario = {'lista':lista, 'listaProcesada':procesada}
    return render(request, template_name, diccionario)
    

def noHome(request):
    print("OwO")

    return HttpResponse("Chan chan chan...")

def nueva(request):
    print("Nueva vista D:")
    
    return HttpResponse("Nueva Vista")

def procesaLista(lista):
    listaNueva = []
    #calculando la norma 
    for i in lista:
        valor = i.temperatura ** 2 + i.color ** 2 + i.inflammation **2 
        resu = valor**0.5
        if resu >25:
            listaNueva.append(resu)
    
    return listaNueva