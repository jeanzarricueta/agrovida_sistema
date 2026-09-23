from django.shortcuts import render
from .data import productos

def mostrar_productos(request):
    context = {
        'productos': productos
    }

    return render(request, 'catalogo/index.html', context)

# Create your views here.
