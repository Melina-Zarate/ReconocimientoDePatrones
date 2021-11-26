from django.shortcuts import render

# Create your views here.
def about(request):
    template_name = "about/about.html"
    nombre = consultaDB(request)
    lista = [1,2,3,4,5]
    return render(request, template_name, {'nombre':nombre, 'miLista':lista})
    

def consultaDB(request):
    #realizamos la petición
    return "Alex"
    