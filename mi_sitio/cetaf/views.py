from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from .forms import SedeForm, AmbienteForm
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView


#
# Vistas Home
#
def index(request):
    return render(request, 'home/index.html')

def acercade(request):
    return render(request, 'home/acercade.html')

def ayuda(request):
    return render(request, 'home/ayuda.html')


#
# CRUD de Usuarios
#
def lts_usuarios(request):
    return render(request, 'usuarios/index.html')


#
# CRUD de las Sedes
#
def lts_sedes(request):
    lista = Sede.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'sedes/index.html', {'obj_pagina': obj_pagina})

def crear_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sedes')
    else:
        form = SedeForm()
        contexto = {
            'form': form
        }
        return render(request, 'sedes/crear_sede.html', contexto)

def detalle_sede(request, _id):
    try:
        sede = Sede.objects.get(pk = _id)
    except Sede.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'sedes/detalle_sede.html', {'sede': sede})

def actualizar_sede(request, _id):
    try:
        dato_old = get_object_or_404(Sede, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/sedes/{_id}/')
    else:
        form = SedeForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'sedes/actualizar_sede.html', contexto)

def borrar_sede(request, _id):
    try:
        data = get_object_or_404(Sede, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        data.delete()
        return redirect('/sedes')
    else:
        return render(request, 'sedes/borrar_sede.html', {'sede': data})


#
# CRUD de las Ambientes
#
def lts_ambiente(request):
    lista = Ambiente.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'ambientes/index.html', {'obj_pagina': obj_pagina})

def crear_ambiente(request):
    if request.method == 'POST':
        form = AmbienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ambientes')
    else:
        form = AmbienteForm()
        contexto = {
            'form': form
        }
        return render(request, 'ambientes/crear_ambiente.html', contexto)

def detalle_ambiente(request, _id):
    try:
        ambiente = Ambiente.objects.get(pk = _id)
    except Ambiente.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'ambientes/detalle_ambiente.html', {'ambiente': ambiente})

def actualizar_ambiente(request, _id):
    try:
        dato_old = get_object_or_404(Ambiente, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        form = AmbienteForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/ambientes/{_id}/')
    else:
        form = AmbienteForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'ambientes/actualizar_ambiente.html', contexto)

def borrar_ambiente(request, _id):
    try:
        data = get_object_or_404(Ambiente, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        data.delete()
        return redirect('/ambientes')
    else:
        return render(request, 'ambientes/borrar_ambiente.html', {'ambiente': data})