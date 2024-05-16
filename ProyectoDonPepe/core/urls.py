from django.urls import path
from .views import inicio, register, productos, quienessomos, galeria, perfil, login

urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
    path('perfil/', perfil, name="perfil"),
    path('login/', login, name="login"),
]