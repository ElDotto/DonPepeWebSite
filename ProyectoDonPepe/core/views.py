from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def register(request):
    if request.method == "POST":
        nombreUser = request.POST.get('nombre')
        apellidoUser = request.POST.get('apellido')
        rutUser = request.POST.get('rut')
        fechaUser = request.POST.get('fechaNacimiento')
        telefonoUser = request.POST.get('telefono')
        emailUser = request.POST.get('email')
        claveUser = request.POST.get('password')
        confclaveUser = request.POST.get('confirmPassword')
        
        # Validaciones
        if Usuario.objects.filter(email=emailUser).exists():
            messages.error(request, "Este correo ya está registrado!")
            return redirect('register') 
                
        usuario = Usuario.objects.create(rut=rutUser, nombre=nombreUser, apellido=apellidoUser, fecha_nacimiento=fechaUser, telefono=telefonoUser, correo=emailUser, clave=claveUser, rol=2)

        messages.success(request, 'Cuenta creada con éxito.')
        
        return redirect('inicio')

    return render(request, 'core/register.html')

def productos(request):
    return render(request, 'core/productos.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def login(request):
    return render(request, 'core/login.html')

def perfil(request):
    return render(request, 'core/perfil.html')