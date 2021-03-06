from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from .forms import SedeForm, AmbienteForm, CategoriaForm, ActivoForm, AsignacionForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
@login_required(login_url="login")
def lts_usuarios(request):
    return render(request, 'usuarios/index.html')


#
# CRUD de las Sedes
#
@login_required(login_url="login")
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
@login_required(login_url="login")
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


#
# CRUD de las Categorias
#
@login_required(login_url="login")
def lts_categoria(request):
    lista = Categoria.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'categorias/index.html', {'obj_pagina': obj_pagina})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
    else:
        form = CategoriaForm()
        contexto = {
            'form': form
        }
        return render(request, 'categorias/crear_categoria.html', contexto)

def detalle_categoria(request, _id):
    try:
        categoria = Categoria.objects.get(pk = _id)
    except Categoria.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'categorias/detalle_categoria.html', {'categoria': categoria})

def actualizar_categoria(request, _id):
    try:
        dato_old = get_object_or_404(Categoria, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/categorias/{_id}/')
    else:
        form = CategoriaForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'categorias/actualizar_categoria.html', contexto)

def borrar_categoria(request, _id):
    try:
        data = get_object_or_404(Categoria, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        data.delete()
        return redirect('/categorias')
    else:
        return render(request, 'categorias/borrar_categoria.html', {'categoria': data})


#
# CRUD de los Activos
#
@login_required(login_url="login")
def lts_activo(request):
    lista = Activo.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'activos/index.html', {'obj_pagina': obj_pagina})

def crear_activo(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/activos')
    else:
        form = ActivoForm()
        contexto = {
            'form': form
        }
        return render(request, 'activos/crear_activo.html', contexto)

def detalle_activo(request, _id):
    try:
        activo = Activo.objects.get(pk = _id)
    except Activo.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'activos/detalle_activo.html', {'activo': activo})

def actualizar_activo(request, _id):
    try:
        dato_old = get_object_or_404(Activo, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        form = ActivoForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/activos/{_id}/')
    else:
        form = ActivoForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'activos/actualizar_activo.html', contexto)

def borrar_activo(request, _id):
    try:
        data = get_object_or_404(Activo, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        data.delete()
        return redirect('/activos')
    else:
        return render(request, 'activos/borrar_activo.html', {'activo': data})


#
# CRUD de las asignaciones
#
@login_required(login_url="login")
def lts_asignacion(request):
    lista = Asignacion.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'asignaciones/index.html', {'obj_pagina': obj_pagina})

def crear_asignacion(request):
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/asignaciones')
    else:
        form = AsignacionForm()
        contexto = {
            'form': form
        }
        return render(request, 'asignaciones/crear_asignacion.html', contexto)

def detalle_asignacion(request, _id):
    try:
        asignacion = Asignacion.objects.get(pk = _id)
    except Asignacion.DoesNotExist:
        raise Http404('Este registro no existe')

    return render(request, 'asignaciones/detalle_asignacion.html', {'asignacion': asignacion})

def actualizar_asignacion(request, _id):
    try:
        dato_old = get_object_or_404(Asignacion, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        form = AsignacionForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/asignaciones/{_id}/')
    else:
        form = AsignacionForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'asignaciones/actualizar_asignacion.html', contexto)

def borrar_asignacion(request, _id):
    try:
        data = get_object_or_404(Asignacion, id = _id)
    except Exception:
        raise Http404('El registro no existe')
    if request.method == 'POST':
        data.delete()
        return redirect('/asignaciones')
    else:
        return render(request, 'asignaciones/borrar_asignacion.html', {'asignacion': data})


#
# Login
#
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Error en credenciales')
            return redirect('login')
    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Saliendo del sistema')
    return redirect('login/')