from django.urls import path
from .views import inicio, register, productos, quienessomos, galeria, login_user, cerrarsesion, editarperfil, actualizarperfil, administrador, agregar, ingresarproducto, listaproducto, listausuarios, borrarperfil, borrarproducto, editarproducto, actualizaproducto, detalleproducto


urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
    path('login_user/', login_user, name="login_user"),
    path('cerrarsesion/', cerrarsesion, name="cerrarsesion"),
    path('editarperfil/', editarperfil, name="editarperfil"),
    path('actualizarperfil/', actualizarperfil, name="actualizarperfil"),
    path('administrador/', administrador, name="administrador"),
    path('agregar/', agregar, name="agregar"),
    path('ingresarproducto/', ingresarproducto, name="ingresarproducto"),
    path('listaproducto/', listaproducto, name="listaproducto"),
    path('listausuarios/', listausuarios, name="listausuarios"),
    path('borrarperfil/<rut>/', borrarperfil, name="borrarperfil"),
    path('borrarproducto/<id_producto>/', borrarproducto, name="borrarproducto"),
    path('editarproducto/<id_producto>/', editarproducto, name="editarproducto"),
    path('actualizaproducto/', actualizaproducto, name="actualizaproducto"),
    path('detalleproducto/<int:pk>', detalleproducto, name="detalleproducto"),
] 