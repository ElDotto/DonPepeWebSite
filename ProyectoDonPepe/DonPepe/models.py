from django.db import models

class Usuario(models.Model):

    rut                 = models.CharField(primary_key=True,max_length=10)
    nombre              = models.CharField(max_length=20)
    apellido            = models.CharField(max_length=20)
    fecha_nacimiento    = models.DateField(blank=False,null=False)
    telefono            = models.CharField(max_length=45)
    correo               = models.EmailField(unique=True,max_length=100, blank=True, null=True)
    clave          = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre  