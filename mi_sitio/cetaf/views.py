from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from django.contrib.auth.models import User, Group
from .forms import SedeForm, AmbienteForm, CategoriaForm, ActivoForm, AsignacionForm, UsuarioForm, PerfilForm, GruposForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db.models import Q
from django.views.generic.list import ListView
import csv


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
# CRUD de las Sedes
#
@login_required(login_url="login")
@permission_required('cetaf.view_sede', raise_exception=True)
def lts_sedes(request):
    lista = Sede.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'sedes/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('cetaf.add_sede', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('cetaf.view_sede', raise_exception=True)
def detalle_sede(request, _id):
    try:
        sede = Sede.objects.get(pk = _id)
    except Sede.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'sedes/detalle_sede.html', {'sede': sede})

@login_required(login_url="login")
@permission_required('cetaf.change_sede', raise_exception=True)
def actualizar_sede(request, _id):
    try:
        dato_old = get_object_or_404(Sede, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
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

@login_required(login_url="login")
@permission_required('cetaf.delete_sede', raise_exception=True)
def borrar_sede(request, _id):
    try:
        data = get_object_or_404(Sede, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        data.delete()
        return redirect('/sedes')
    else:
        return render(request, 'sedes/borrar_sede.html', {'sede': data})


#
# CRUD de las Ambientes
#
@login_required(login_url="login")
@permission_required('cetaf.view_ambiente', raise_exception=True)
def lts_ambiente(request):
    lista = Ambiente.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'ambientes/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('cetaf.add_ambiente', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('cetaf.view_ambiente', raise_exception=True)
def detalle_ambiente(request, _id):
    try:
        ambiente = Ambiente.objects.get(pk = _id)
    except Ambiente.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'ambientes/detalle_ambiente.html', {'ambiente': ambiente})

@login_required(login_url="login")
@permission_required('cetaf.change_ambiente', raise_exception=True)
def actualizar_ambiente(request, _id):
    try:
        dato_old = get_object_or_404(Ambiente, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
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

@login_required(login_url="login")
@permission_required('cetaf.delete_ambiente', raise_exception=True)
def borrar_ambiente(request, _id):
    try:
        data = get_object_or_404(Ambiente, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        data.delete()
        return redirect('/ambientes')
    else:
        return render(request, 'ambientes/borrar_ambiente.html', {'ambiente': data})


#
# CRUD de las Categorias
#
@login_required(login_url="login")
@permission_required('cetaf.view_categoria', raise_exception=True)
def lts_categoria(request):
    lista = Categoria.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'categorias/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('cetaf.add_categoria', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('cetaf.view_categoria', raise_exception=True)
def detalle_categoria(request, _id):
    try:
        categoria = Categoria.objects.get(pk = _id)
    except Categoria.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'categorias/detalle_categoria.html', {'categoria': categoria})

@login_required(login_url="login")
@permission_required('cetaf.change_categoria', raise_exception=True)
def actualizar_categoria(request, _id):
    try:
        dato_old = get_object_or_404(Categoria, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
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

@login_required(login_url="login")
@permission_required('cetaf.delete_categoria', raise_exception=True)
def borrar_categoria(request, _id):
    try:
        data = get_object_or_404(Categoria, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        data.delete()
        return redirect('/categorias')
    else:
        return render(request, 'categorias/borrar_categoria.html', {'categoria': data})


#
# CRUD de los Activos
#
@login_required(login_url="login")
@permission_required('cetaf.view_activo', raise_exception=True)
def lts_activo(request):
    lista = Activo.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'activos/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('cetaf.add_activo', raise_exception=True)
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

@login_required(login_url="login")
@permission_required('cetaf.view_activo', raise_exception=True)
def detalle_activo(request, _id):
    try:
        activo = Activo.objects.get(pk = _id)
    except Activo.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'activos/detalle_activo.html', {'activo': activo})

@login_required(login_url="login")
@permission_required('cetaf.change_activo', raise_exception=True)
def actualizar_activo(request, _id):
    try:
        dato_old = get_object_or_404(Activo, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
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

@login_required(login_url="login")
@permission_required('cetaf.delete_activo', raise_exception=True)
def borrar_activo(request, _id):
    try:
        data = get_object_or_404(Activo, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        data.delete()
        return redirect('/activos')
    else:
        return render(request, 'activos/borrar_activo.html', {'activo': data})


#
# CRUD de las asignaciones
#
@login_required(login_url="login")
@permission_required('cetaf.view_asignacion', raise_exception=True)
def lts_asignacion(request):
    lista = Asignacion.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'asignaciones/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('cetaf.add_asignacion', raise_exception=True)
def crear_asignacion(request):
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/asignaciones')
        else:
            messages.info(request, 'El elemento ya ha sido asignado')
            return redirect('/asignaciones/crear')
    else:
        form = AsignacionForm()
        contexto = {
            'form': form
        }
        return render(request, 'asignaciones/crear_asignacion.html', contexto)

@login_required(login_url="login")
@permission_required('cetaf.view_asignacion', raise_exception=True)
def detalle_asignacion(request, _id):
    try:
        asignacion = Asignacion.objects.get(pk = _id)
    except Asignacion.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'asignaciones/detalle_asignacion.html', {'asignacion': asignacion})

@login_required(login_url="login")
@permission_required('cetaf.change_asignacion', raise_exception=True)
def actualizar_asignacion(request, _id):
    try:
        dato_old = get_object_or_404(Asignacion, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        form = AsignacionForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            return redirect(f'/asignaciones/{_id}/')
        else:
            messages.info(request, 'El elemento ya ha sido asignado')
            return redirect(f'/asignaciones/{_id}/actualizar')
    else:
        form = AsignacionForm(instance=dato_old)
        contexto = {
            'form': form
        }
        return render(request, 'asignaciones/actualizar_asignacion.html', contexto)

@login_required(login_url="login")
@permission_required('cetaf.delete_asignacion', raise_exception=True)
def borrar_asignacion(request, _id):
    try:
        data = get_object_or_404(Asignacion, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        data.delete()
        return redirect('/asignaciones')
    else:
        return render(request, 'asignaciones/borrar_asignacion.html', {'asignacion': data})

#
# CRUD Usuarios
#
@login_required(login_url="login")
@permission_required('auth.add_user', raise_exception=True)
def crear_usuarios(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'usuarios/crear_usuario.html',{'form':form})

@login_required(login_url="login")
@permission_required('auth.change_user', raise_exception=True)
def editar_usuarios(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Actualizacion realizada con exito')
            return redirect(f'/usuarios/editar')
        else:
            messages.info(request, 'Error en guardado')
            return redirect(f'/usuarios/editar') 
    else:
        form = UsuarioForm(instance=request.user)
    return render(request, 'usuarios/editar_usuario.html', {'form':form})

@login_required(login_url="login")
def editar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Actualizacion realizada con exito')
            return redirect(f'/usuarios/editar_perfil')
        else:
            messages.info(request, 'Error en guardado')
            return redirect(f'/usuarios/editar_perfil') 
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form':form})

@login_required(login_url="login")
def cambiar_password(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Cambio de contraseña realizado con exito')
            return redirect(f'/usuarios/password')
        else:
            messages.info(request, 'Error en el cambio de contraseña')
            return redirect(f'/usuarios/password') 
    else:
        form = SetPasswordForm(request.user, request.POST)
    return render(request, 'usuarios/password.html', {'form':form})

#
# Tipos de usuario / Grupos [Permisos]
#
@login_required(login_url="login")
@permission_required('auth.view_user', raise_exception=True)
def lts_usuarios(request):
    lista = User.objects.all()
    paginador = Paginator(lista, 10)
    num_pagina = request.GET.get('page')
    obj_pagina = paginador.get_page(num_pagina)

    return render(request, 'tipo_usuarios/index.html', {'obj_pagina': obj_pagina})

@login_required(login_url="login")
@permission_required('auth.add_user', raise_exception=True)
def crear_grupo(request):
    if request.method == "POST":
        form = GruposForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Grupo creado con exito')
            return redirect(f'/tipo_usuarios/crear')
        else:
            messages.info(request, 'Error al crear el grupo')
            return redirect(f'/tipo_usuarios/crear') 
    else:
        form = GruposForm()
    return render(request, 'tipo_usuarios/crear_grupos.html', {'form':form})

@login_required(login_url="login")
@permission_required('auth.change_user', raise_exception=True)
def actualizar_permisos(request, _id):
    try:
        dato_old = get_object_or_404(User, id = _id)
    except Exception:
        return render(request, '404.html', status=404)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=dato_old)
        if form.is_valid():
            form.save()
            messages.info(request, 'Actualizacion realizada con exito')
            return redirect(f'/tipo_usuarios/{_id}/editar')
        else:
            messages.info(request, 'Error en guardado')
            return redirect(f'/tipo_usuarios/{_id}/editar') 
    else:
        form = UsuarioForm(instance=dato_old)
    return render(request, 'tipo_usuarios/actualizar_permisos.html', {'form':form})


#
# Consultas / Reportes
#
@login_required(login_url="login")
@permission_required('cetaf.view_consulta', raise_exception=True)

def lts_consulta(request):
    return render(request, 'consultas/index.html')


@login_required(login_url="login")
@permission_required('cetaf.view_consulta', raise_exception=True)

def filtrar_consulta(request):
    consulta = request.GET.get('buscar')
    global lts_filtrada
    lts_filtrada = Asignacion.objects.filter(
        Q(nombre_activo__nombre__icontains=consulta) | Q(persona_responsable__icontains=consulta) | Q(nombre_activo__categoria__nombre__icontains=consulta)
        | Q(sede_asignada__nombre__icontains=consulta) | Q(ambiente_asignado__nombre__icontains=consulta)
    )
    return render(request, 'consultas/index.html', {'lts_filtrada': lts_filtrada})

@login_required(login_url="login")
@permission_required('cetaf.view_consulta', raise_exception=True)
def detalle_consulta(request, _id):
    try:
        consulta = Asignacion.objects.get(pk = _id)
    except Asignacion.DoesNotExist:
        return render(request, '404.html', status=404)

    return render(request, 'consultas/detalle_consulta.html', {'consulta': consulta})


@login_required(login_url="login")
@permission_required('cetaf.view_consulta', raise_exception=True)

def exportar_asignacion(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Asignaciones.csv"'},
    )

    escribir = csv.writer(response)
    escribir.writerow(['Nombre activo', 'Persona responsable', 'Sede asignado', 'Ambiente asignado', 'Fecha inicio', 'fecha fin', 'descripcion'])
    asignaciones = lts_filtrada.values_list('nombre_activo__nombre', 'persona_responsable', 'sede_asignada', 'ambiente_asignado', 'fecha_inicio', 'fecha_fin', 'descripcion')

    for asignacion in asignaciones:
        escribir.writerow(asignacion)

    return response


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
