from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios

# Create your models here.
#Categoría. Se la define primero para hacer una relación con los artículos.-
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    imagen = models.ImageField(null=True, upload_to='categorias', default='categorias/album_default.png')
    
    def __str__(self):
        return self.nombre

   
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now, blank = True)
    texto = models.TextField(null = False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=None)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    
    def get_default_categoria():
        return Categoria.objects.get_or_create(nombre='Sin Categoría')[0]
    
    
    class Meta:
        ordering = ('-publicado',)
    
    def __str__(self, using = None, keep_parents =False):
        self.imagen.delete(self.imagen.name)
        super().delete()


