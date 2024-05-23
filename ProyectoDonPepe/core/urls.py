from django.urls import path
from .views import inicio, register, productos, quienessomos, galeria, editarperfil, login_user, cerrarsesion
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
    path('editarperfil/', editarperfil, name="editarperfil"),
    path('login_user/', login_user, name="login_user"),
    path('cerrarsesion/', cerrarsesion, name="cerrarsesion"),
] 