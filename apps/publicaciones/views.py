from typing import Any
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView


from .models import Categoria, Publicaciones
from apps.comentarios.models import Comentario
from apps.comentarios.forms import OpinionForm


# Create your views here.

class AgregarCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'publicaciones/agregar_categoria.html'
    success_url = reverse_lazy('inicio')

class AgregarPublicacion(CreateView):
    model = Publicaciones
    fiels = ['titulo','subtitulo', 'fecha','texto', 'activo', 'categoria', 'imagen', 'publicado']
    template_name = 'publicaciones/agregar_publicaciones.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self,form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)

class ModificarPublicacion(UpdateView):
    model = Publicaciones
    fields = ['titulo','subtitulo', 'fecha','texto', 'activo', 'categoria', 'imagen', 'publicado']
    template_name = 'publicaciones/agregar_publicacion.html'
    success_url = reverse_lazy('inicio')

class ListarPublicacion(ListView):
    model = Publicaciones
    template_name = 'publicaciones/listar_publicaciones.html'
    context_object_name = 'publicaciones'
    paginate_by = 3

    def get_context_data(self) :
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains = query)
        return queryset.order_by('fecha')

class EliminarPublicacion(DeleteView):
    model = Publicaciones
    template_name = 'publicaciones/confirma_eliminar.html'
    success_url = reverse_lazy('inicio')

def publicacion_detalle(request,id):
    publicaciones = Publicaciones.objects.get(id=id)
    comentarios = Comentarios.objects.filter(publicacion=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.publicacion = publicacion
            aux.usuario = request.user
            aux.save()
            detalle_url = reverse('apps.publicaciones:detalle_publicacion', kwargs={'id': publicacion.id})
            return HttpResponseRedirect(detalle_url)
        else:
            return redirect('apps.usuarios:iniciar_sesion')
    
    contexto = {
        'publicacion': publicacion,
        'form': form,
        'ocomentarios': comentarios
    }
    template_name = 'publicaciones/publicacion_detalle.html'
    return render(request,template_name,contexto)


def listar_por_categoria(request, categoria):
    categoria = Categoria.objects.filter(nombre = categoria)
    publicaciones = Publicaciones.objects.filter(categoria = categoria[0].id).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = 'publicaciones/listar_publicaciones.html'
    contexto = {
        'publicaciones' : publicaciones,
        'categorias' : categorias        
    }
    return render(request,template_name,contexto)

# -----------Ejemplo de : Ordenar por  ----------------------

def ordenar_por(request):
    # Obtenemos el dato de 'orden' de la URL -> metodo GET ( para esto tiene que haber un elemento html que contenga el name = 'orden' y el valor(value=''))
    orden = request.GET.get('orden', '')
    #Validar lo que contiene Value
    if orden == 'fecha':
        publicaciones = Publicaciones.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        publicaciones = Publicaciones.objects.order_by('titulo')
    else:
        Publicaciones = Publicaciones.objects.all()
    categorias = Categoria.objects.all()
    template_name = 'publicaciones/listar_publicaciones.html'
    contexto = {
        'publicaciones' : publicaciones,
        'categorias' : categorias,
    }
    return render(request, template_name, contexto)