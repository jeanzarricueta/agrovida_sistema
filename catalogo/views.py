from django.shortcuts import render
from .dataimport productos

def mostrar_productos(request):
    context = {
        'productos': productos
    }

    return render(request, 'catalogo/index.html', contexto)

# Create your views here.
