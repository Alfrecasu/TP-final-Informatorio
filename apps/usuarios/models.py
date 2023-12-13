from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here. El usuario debe poder loguearse para realizar opiniones/comentarios

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length= 20)
    fecha_nacimiento = models.DateField('Fecha_nacimiento', default = '2000-1-1')
    es_colaborador = models.BooleanField(default=False) #Se determina al usuario colaborador con un booleano
    imagen = models.ImageField(null = True, blank = True, upload_to = 'usuarios', default='usuarios/default.png')#Esta imagen se la guarda dentro de la carpeta media

def __str__(self):
    return self.nombre
