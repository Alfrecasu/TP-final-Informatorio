from django.urls import path
from .views import AgregarComentario,ModificarComentario,EliminarComentario

app_name = 'apps.comentarios'

urlpatterns = [
    path('agregar_comentario/', AgregarComentario, name='agregar_comentario'),
    path('modificar_comentario/<int:pk>', ModificarComentario.as_view(), name='modificar_comentario'),
    path("eliminar_cementario/<int:pk>", EliminarComentario.as_view(), name='eliminar_comentario'),
]