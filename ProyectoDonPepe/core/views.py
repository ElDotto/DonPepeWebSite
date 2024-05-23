from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario, Producto, Venta, Categoria, DetalleVenta, Rol, Region, Comuna, Direccion


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def register(request):
    if request.method == "POST":
        nombreUser = request.POST['nombre']
        apellidoUser = request.POST['apellido']
        rutUser = request.POST['rut']
        telefonoUser = request.POST['telefono']
        emailUser = request.POST['email']
        claveUser = request.POST['password']
        confclaveUser = request.POST['confirmPassword']
        
        # Validaciones
        if User.objects.filter(username=emailUser).exists():
            messages.error(request, "Este correo ya está registrado!")
            return redirect('register')
        
        if Usuario.objects.filter(rut=rutUser).exists():
            messages.error(request, "Este RUT ya está registrado!")
            return redirect('register')
        
        if claveUser != confclaveUser:
            messages.error(request, "La contraseña no coincide")
            return redirect('register')
                
        rol = Rol.objects.get(idRol=2)  # Suponiendo que el rol "2" es el rol que deseas asignar
        usuario = Usuario.objects.create(rut=rutUser, nombre=nombreUser, apellido=apellidoUser, telefono=telefonoUser, correo=emailUser, clave=confclaveUser, rol=rol)

        user = User.objects.create_user(username = emailUser, email=emailUser, password= claveUser)
        user.first_name = nombreUser
        user.last_name = apellidoUser
        user.is_staff = True
        user.save()
        messages.success(request, 'Cuenta creada con éxito.')
        
        return redirect('inicio')

    return render(request, 'core/register.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(request, username=email, password=password)
        print("Usuario autenticado: ", user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('inicio')  # Redirigir a la página de inicio o a la página deseada
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    return render(request, 'core/login_user.html')


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categorias.html', {'categorias': categorias})


def regiones(request):
    regiones = Region.objects.all()
    return render(request, 'core/regiones.html', {'regiones': regiones})

def comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'core/comunas.html', {'comunas': comunas})

def direcciones(request):
    direcciones = Direccion.objects.all()
    return render(request, 'core/direcciones.html', {'direcciones': direcciones})

def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'core/ventas.html', {'ventas': ventas})

def detalles_venta(request):
    detalles_venta = DetalleVenta.objects.all()
    return render(request, 'core/detalles_venta.html', {'detalles_venta': detalles_venta})

@login_required
def productos(request, categoria_id=None):
    if categoria_id is not None:
        categoria = Categoria.objects.get(pk=categoria_id)
        productos = categoria.producto_set.all()
    else:
        productos = Producto.objects.all()
        categoria = None
    categorias = Categoria.objects.all()
    
    # Convertir el precio de cada producto al formato deseado (215000)
    for producto in productos:
        producto.precio = str(int(producto.precio))
    
    return render(request, 'core/productos.html', {'productos': productos, 'categorias': categorias, 'categoria_actual': categoria})


def quienessomos(request):
    return render(request, 'core/quienessomos.html')

@login_required
def galeria(request):
    return render(request, 'core/galeria.html')



def editarperfil(request):
    return render(request, 'core/editarperfil.html')

def cerrarsesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente!!")
    return redirect('inicio')





