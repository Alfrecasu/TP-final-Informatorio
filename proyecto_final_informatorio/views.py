from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {'nombre': 'Informatorio'}
    return render(request, template_name, context)

def contacto(request):
    template_name = 'contacto.html'
    nombres = ['Informatorio', 'Grupo 6', 'Alfre Casu', 'Matias Melga'] #En caso de pasar una lista de nombres -> cambiar en contactos 
    context = {'nombres': nombres}
    return render(request, template_name, context)


