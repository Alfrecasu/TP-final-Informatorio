from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios

# Create your models here.
#Categoría. Se la define primero para hacer una relación con los artículos.-
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    imagen = models.ImageField(null=True, upload_to='categorias', default='categorias/post_default.png')
    
    def __str__(self):
        return self.nombre

   
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now, blank = True)
    texto = models.TextField(null = False)
    activo = models.BooleanField(default=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True,default=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=None)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')

    
    
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-fecha',)
    
   

