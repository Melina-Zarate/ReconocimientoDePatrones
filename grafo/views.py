from django.shortcuts import render
from home.models import Tejido
import math
import numpy as np


# Create your views here.
def grafo(request):
    lista = Tejido.objects.get_queryset()
    #lista normas
    normas = procesaLista(lista)
    
    resu = distEuclidia(normas)
    resu = np.reshape(resu, (len(normas), len(normas)))
    template_name = "grafo.html"
    diccionario = {"resultado": resu}
    return render(request, template_name, diccionario)


def procesaLista(lista):
    listaNueva = []
    #calculando la norma 
    for i in lista:
        valor = i.temperatura ** 2 + i.color ** 2 + i.inflammation **2 
        resu = valor**0.5
        if resu >25:
            listaNueva.append(resu)
    
    return listaNueva


def distEuclidia(datos):
    lista = []
    for elemento1 in range(len(datos)):
        for elemento2 in range(len(datos)):
            dist = ( datos[elemento1] - datos[elemento2] )
            euclidiana = math.sqrt(pow(dist, 2))
            lista.append(euclidiana)
        print("\n")
    return lista
