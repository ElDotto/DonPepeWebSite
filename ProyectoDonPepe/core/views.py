from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def register(request):
    return render(request, 'core/register.html')

def productos(request):
    return render(request, 'core/productos.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def galeria(request):
    return render(request, 'core/galeria.html')