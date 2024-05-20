from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Producto, Venta, Categoria, DetalleVenta, Rol, Region, Comuna, Direccion


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def register(request):
    if request.method == "POST":
        nombreUser = request.POST.get('nombre')
        apellidoUser = request.POST.get('apellido')
        rutUser = request.POST.get('rut')
        telefonoUser = request.POST.get('telefono')
        emailUser = request.POST.get('email')
        claveUser = request.POST.get('password')
        confclaveUser = request.POST.get('confirmPassword')
        
        # Validaciones
        if Usuario.objects.filter(correo=emailUser).exists():
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

        messages.success(request, 'Cuenta creada con éxito.')
        
        return redirect('inicio')

    return render(request, 'core/register.html')

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

def galeria(request):
    return render(request, 'core/galeria.html')

def login(request):
    return render(request, 'core/login.html')

def perfil(request):
    return render(request, 'core/perfil.html')

