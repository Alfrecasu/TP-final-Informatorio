from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuarios
from .forms import RegistrarUsuariosForm

# Create your views here.
class RegistrarUsuario(CreateView):
    model = Usuarios
    form_class = RegistrarUsuariosForm
    template_name = 'usuarios/registrar_usuarios.html'
    successs_url = reverse_lazy('inicio')

class ActualizarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuarios
    fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento', 'imagen']
    template_name = 'usuarios/registrar_usuarios.html'
    successs_url = reverse_lazy('inicio')

class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuarios
    template_name = 'publicaciones/confirmar_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios" : usuarios
    }
    return render(request, template_name, contexto)
