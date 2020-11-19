from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from .forms import SedeForm
from django.views.generic.edit import CreateView

# Create your views here.
# Vistas Home
def index(request):
    return render(request, 'home/index.html')

def acercade(request):
    return render(request, 'home/acercade.html')

def ayuda(request):
    return render(request, 'home/ayuda.html')


# CRUD de Usuarios
def lts_usuarios(request):
    return render(request, 'usuarios/index.html')

# CRUD de las Sedes
def lts_sedes(request):
    lista = Sede.objects.all()
    template = loader.get_template('sedes/index.html')
    contexto = {
        'lista_sedes': lista,
    }
    return HttpResponse(template.render(contexto, request))

def crear_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sedes')
    else:
        form = SedeForm()
        contexto = {
            'form':form
        }
        return render(request, 'sedes/crear_sede.html', contexto)

def detalle_sede(request, _id):
    try:
        sede = Sede.objects.get(pk = _id)
    except Sede.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'sedes/detalle_sede.html', {'sede':sede})