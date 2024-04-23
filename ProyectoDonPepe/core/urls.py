from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('register/', views.register, name="register"),
    path('productos/', views.productos, name="productos"),
    path('quienessomos/', views.quienessomos, name="quienessomos"),
    path('galeria/', views.galeria, name="galeria"),
]