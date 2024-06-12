from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario, Producto, Venta, Categoria, DetalleVenta, Rol, Region, Comuna, Direccion


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    
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
        
        return redirect('login_user')

    return render(request, 'core/register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(request, username=email, password=password)
        print("Usuario autenticado: ", user)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Verificar si el usuario es un superusuario
                # Asignar el rol de administrador al superusuario
                rol_administrador = Rol.objects.get(idRol=1)  # Suponiendo que el id del rol de administrador es 1
                user.rol = rol_administrador
            else:
                # Asignar el rol de usuario al usuario normal
                rol_usuario = Rol.objects.get(idRol=2)  # Suponiendo que el id del rol de usuario es 2
                user.rol = rol_usuario
            user.save()
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('inicio')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'core/login_user.html')

def cerrarsesion(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente!!")
    return redirect('inicio')


@login_required
def editarperfil(request):
    user = request.user
    usuario = Usuario.objects.get(correo=user.username)
    context = {
        'usuario': usuario
    }
    return render(request, 'core/editarperfil.html', context)

@login_required
def actualizarperfil(request):
    user = request.user
    usuario = Usuario.objects.get(correo=user.username)
    if request.method == "POST":
        nombreUsuario = request.POST['nombre']
        apellidoUsuario = request.POST['apellido']
        telefonoUsuario = request.POST['telefono']
        emailUsuario = request.POST['email']
        
        # Verificar si el correo electrónico ha sido cambiado
        if emailUsuario != user.username:
            # Si el nuevo correo electrónico es diferente al actual del usuario, realizar validación
            if User.objects.filter(username=emailUsuario).exists():
                messages.error(request, "Este correo ya está registrado!")
                return redirect('editarperfil')
        
        usuario.nombre = nombreUsuario
        usuario.apellido = apellidoUsuario
        usuario.telefono = telefonoUsuario
        usuario.correo = emailUsuario
        user.username = emailUsuario
        user.email= emailUsuario
        
        usuario.save()
        user.save()

        messages.success(request, 'Cuenta actualizada con éxito.')
        return redirect('editarperfil')
    
    context = {
        'usuario': usuario
    }
    return render(request, 'core/editarperfil.html', context)


def administrador(request):
    return render(request, 'core/administrador.html')

def agregar(request):
    categoriaProducto = Categoria.objects.all()
    contexto = {
        "categorias" : categoriaProducto
    }

    return render(request, 'core/agregar.html', contexto)

def ingresarproducto(request):

    idProducto = request.POST['id']
    nombreProducto = request.POST['nombre']
    stockProducto = request.POST['stock']
    descripcion = request.POST['descripcion']
    foto = request.FILES['foto']
    precio = request.POST['precio']
    categoria = request.POST['categoria']

    categoriaP= Categoria.objects.get(idCategoria= categoria)

    producto = Producto.objects.create(codProducto= idProducto, nombreP= nombreProducto, stock= stockProducto, descipcion= descripcion, foto= foto, precio= precio, categoria= categoriaP)
    messages.success(request, 'Producto ingresado correctamente.')
    return redirect('agregar')

def listaproducto(request):
    productoListado = Producto.objects.all()
    categorias= Categoria.objects.all()
    contexto = {
        "categorias": categorias,
        "productos": productoListado
    }   
    return render(request, 'core/listaproducto.html', contexto)

def editarproducto(request, id_producto):
    producto = Producto.objects.get(codProducto = id_producto)
    listaCategoria = Categoria.objects.all()
    contexto = {
        "producto" : producto,
        "listacategoria" : listaCategoria
    }
    return render(request, 'core/editarproducto.html', contexto)

def actualizaproducto(request):
    if request.method == "POST":
        idProducto = request.POST['id']
        nombreProducto = request.POST['nombre']
        stockProducto = request.POST['stock']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']

        producto = Producto.objects.get(codProducto=idProducto)
        categoriaP = Categoria.objects.get(idCategoria=categoria)

        producto.nombreP = nombreProducto
        producto.stock = stockProducto
        producto.descipcion = descripcion
        producto.precio = precio
        producto.categoria = categoriaP

        if 'imagen' in request.FILES:
            producto.foto = request.FILES['imagen']

        producto.save()
        return redirect('listaproducto')


def borrarproducto(request, id_producto):
    productoborrar = Producto.objects.get(codProducto = id_producto)
    productoborrar.delete()
    messages.success(request, 'Producto eliminado correctamente.')
    return redirect('listaproducto')


def listausuarios(request):
    usuariosListado = Usuario.objects.exclude(rut=None).exclude(rut='').all()
    contexto = {
        "usuarios": usuariosListado
    }
    return render(request, 'core/listausuarios.html', contexto)

def borrarperfil(request, rut):
    perfilborrar = Usuario.objects.get(rut = rut)
    perfilborrar.delete()
    messages.success(request, 'Perfil eliminado correctamente.')
    return redirect('listausuarios')

@login_required 
def productos(request):
    productoListado = Producto.objects.all()
    contexto = {
        "productos": productoListado
    }   
    return render(request, 'core/productos.html', contexto)

def detalleproducto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render (request, 'core/detalleproducto.html', {'producto': producto})

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def galeria(request):
    return render(request, 'core/galeria.html')











