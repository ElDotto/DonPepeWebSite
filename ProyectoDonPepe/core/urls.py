from django.urls import path
from .views import inicio, register, productos, quienessomos, galeria, login_user, cerrarsesion, editarperfil, actualizarperfil, administrador, agregar, ingresarproducto


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
] 