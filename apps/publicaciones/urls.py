from django.urls import path
from .views import AgregarCategoria,AgregarPublicacion, ModificarPublicacion,ListarPublicacion,EliminarPublicacion,publicacion_detalle, listar_por_categoria, ordenar_por

app_name='apps.publicaciones'

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name='agregar_categoria'),
    path("agregar_publicacion/", AgregarPublicacion.as_view(), name='agregar_publicacion'),
    path("listar_publicaciones/", ListarPublicacion.as_view(), name='listar_publicaciones'),
    path("modificar_publicacion/<int:pk>", ModificarPublicacion.as_view(), name='modificar_publicacion'),
    path("eliminar_publicacion/<int:pk>", EliminarPublicacion.as_view(), name='eliminar_publicacion'),
    path("detalle_publicacion/<int:id>", publicacion_detalle, name='detalle_publicacion'),
    path("listar_por_categoria/<str:categoria>", listar_por_categoria, name='listar_por_categoria'),
    path("ordenar_por/", ordenar_por, name='ordenar_por'),   
]