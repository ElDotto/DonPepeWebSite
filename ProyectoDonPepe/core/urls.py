from django.urls import path
from .views import inicio, register, productos, quienessomos, galeria

urlpatterns = [
    path('', inicio, name="inicio"),
    path('register/', register, name="register"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('galeria/', galeria, name="galeria"),
]