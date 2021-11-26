from django.shortcuts import render
from home.views import Tejido

# Create your views here.
def sintactico(request):
    lista = Tejido.objects.get_queryset()
    procesada = procesaLista(lista)
    template_name = "sintactico/sintactico.html"
    diccionario = {'lista':lista, 'listaProcesada':procesada}
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