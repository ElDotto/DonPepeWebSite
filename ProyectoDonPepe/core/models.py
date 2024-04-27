
from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreRol

class Usuario(models.Model):

    rut                 = models.CharField(primary_key=True,max_length=10)
    nombre              = models.CharField(max_length=20)
    apellido            = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False,null=False)
    telefono            = models.CharField(max_length=9)
    correo               = models.EmailField(unique=True,max_length=100, blank=True, null=True)
    clave          = models.CharField(max_length=30)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.nombre  

class Region(models.Model):
    idRegion =models.AutoField(primary_key=True)
    nombreR = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreR

class Comuna(models.Model):
    idComuna =models.AutoField(primary_key=True)
    nombreC = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreC

class Direccion(models.Model):
    idDireccion =models.AutoField(primary_key=True)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()

    def __str__(self) -> str:
        return self.calle

class Venta(models.Model):
    codVenta = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fVenta = models.DateField(verbose_name='Fecha de la venta')
    fEntrega = models.DateField(verbose_name='Fecha de la entrega')
    estadoP = models.IntegerField(verbose_name='estado del producto')
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    total = models.IntegerField()
    carrito = models.IntegerField()
    status = models.IntegerField()

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCa = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCa

class Producto(models.Model):
    codProducto = models.AutoField(primary_key=True)
    nombreP = models.CharField(max_length=20)
    stock = models.IntegerField()
    descipcion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="")
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreP

class DetalleVenta(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()