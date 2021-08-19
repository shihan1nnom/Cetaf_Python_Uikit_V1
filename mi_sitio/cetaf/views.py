from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from django.contrib.auth.models import User, Group
from .forms import *
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
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
decoradores = [login_required(login_url="login"), permission_required('cetaf.view_sede', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_sedes(ListView):
    model = Sede
    template_name = 'sedes/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.add_sede', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_sede(CreateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sedes/crear_sede.html'
    success_url = reverse_lazy('lts_sedes')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.view_sede', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class detalle_sede(DetailView):
    model = Sede
    template_name = 'sedes/detalle_sede.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.change_sede', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_sede(UpdateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sedes/actualizar_sede.html'
    success_url = reverse_lazy('lts_sedes')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.delete_sede', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class borrar_sede(DeleteView):
    model = Sede
    template_name = 'sedes/borrar_sede.html'
    success_url = reverse_lazy('lts_sedes')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Elemento eliminado con exito")
        return super().delete(request, *args, **kwargs)


#
# CRUD de las Ambientes
#
decoradores = [login_required(login_url="login"), permission_required('cetaf.view_ambiente', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_ambiente(ListView):
    model = Ambiente
    template_name = 'ambientes/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

decoradores = [login_required(login_url="login"), permission_required('cetaf.add_ambiente', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_ambiente(CreateView):
    model = Ambiente
    form_class = AmbienteForm
    template_name = 'ambientes/crear_ambiente.html'
    success_url = reverse_lazy('lts_ambiente')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        return super().form_invalid(form)



decoradores = [login_required(login_url="login"), permission_required('cetaf.view_ambiente', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class detalle_ambiente(DetailView):
    model = Ambiente
    template_name = 'ambientes/detalle_ambiente.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.change_ambiente', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_ambiente(UpdateView):
    model = Ambiente
    form_class = AmbienteForm
    template_name = 'ambientes/actualizar_ambiente.html'
    success_url = reverse_lazy('lts_ambiente')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.delete_ambiente', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class borrar_ambiente(DeleteView):
    model = Ambiente
    template_name = 'ambientes/borrar_ambiente.html'
    success_url = reverse_lazy('lts_ambiente')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Elemento eliminado con exito")
        return super().delete(request, *args, **kwargs)


#
# CRUD de las Categorias
#
decoradores = [login_required(login_url="login"), permission_required('cetaf.view_categoria', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_categoria(ListView):
    model = Categoria
    template_name = 'categorias/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.add_categoria', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_categoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/crear_categoria.html'
    success_url = reverse_lazy('lts_categoria')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.view_categoria', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class detalle_categoria(DetailView):
    model = Categoria
    template_name = 'categorias/detalle_categoria.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.change_categoria', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_categoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/actualizar_categoria.html'
    success_url = reverse_lazy('lts_categoria')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.delete_categoria', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class borrar_categoria(DeleteView):
    model = Categoria
    template_name = 'categorias/borrar_categoria.html'
    success_url = reverse_lazy('lts_categoria')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Elemento eliminado con exito")
        return super().delete(request, *args, **kwargs)


#
# CRUD de los Activos
#
decoradores = [login_required(login_url="login"), permission_required('cetaf.view_activo', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_activo(ListView):
    model = Activo
    template_name = 'activos/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.add_activo', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_activo(CreateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'activos/crear_activo.html'
    success_url = reverse_lazy('lts_activo')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.view_activo', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class detalle_activo(DetailView):
    model = Activo
    template_name = 'activos/detalle_activo.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.change_activo', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_activo(UpdateView):
    model = Activo
    form_class = ActivoForm
    template_name = 'activos/actualizar_activo.html'
    success_url = reverse_lazy('lts_activo')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.delete_activo', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class borrar_activo(DeleteView):
    model = Activo
    template_name = 'activos/borrar_activo.html'
    success_url = reverse_lazy('lts_activo')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Elemento eliminado con exito")
        return super().delete(request, *args, **kwargs)


#
# CRUD de las asignaciones
#
decoradores = [login_required(login_url="login"), permission_required('cetaf.view_asignacion', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_asignacion(ListView):
    model = Asignacion
    template_name = 'asignaciones/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.add_asignacion', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_asignacion(CreateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'asignaciones/crear_asignacion.html'
    success_url = reverse_lazy('lts_asignacion')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.view_asignacion', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class detalle_asignacion(DetailView):
    model = Asignacion
    template_name = 'asignaciones/detalle_asignacion.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('cetaf.change_asignacion', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_asignacion(UpdateView):
    model = Asignacion
    form_class = AsignacionForm
    template_name = 'asignaciones/actualizar_asignacion.html'
    success_url = reverse_lazy('lts_asignacion')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        return super().form_invalid(form)


decoradores = [login_required(login_url="login"), permission_required('cetaf.delete_asignacion', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class borrar_asignacion(DeleteView):
    model = Asignacion
    template_name = 'asignaciones/borrar_asignacion.html'
    success_url = reverse_lazy('lts_asignacion')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Elemento eliminado con exito")
        return super().delete(request, *args, **kwargs)

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
