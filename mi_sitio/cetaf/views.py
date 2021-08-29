from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import *
from django.contrib.admin.options import *
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
from django.views.generic import ListView, DetailView, FormView
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
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crea nuevo elemento')
        return super().form_invalid(form)

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )


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
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


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
        obj = super(borrar_sede, self).get_object()
        obj_display = str(obj)
        self.log_deletion(self.request, obj, obj_display)
        return super().delete(request, *args, **kwargs)

    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import DELETION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )


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
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crea nuevo elemento')
        return super().form_invalid(form)

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )



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
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


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
        obj = super(borrar_ambiente, self).get_object()
        obj_display = str(obj)
        self.log_deletion(self.request, obj, obj_display)
        return super().delete(request, *args, **kwargs)

    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import DELETION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )


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
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crea nuevo elemento')
        return super().form_invalid(form)

    
    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )



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
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)


    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )    


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
        obj = super(borrar_categoria, self).get_object()
        obj_display = str(obj)
        self.log_deletion(self.request, obj, obj_display)
        return super().delete(request, *args, **kwargs)

    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import DELETION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )


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
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crea nuevo elemento')
        return super().form_invalid(form)

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )


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
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


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
        obj = super(borrar_activo, self).get_object()
        obj_display = str(obj)
        self.log_deletion(self.request, obj, obj_display)
        return super().delete(request, *args, **kwargs)

    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import DELETION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )


#
# Registro Y monitoreo
#
class historial(ListView):
    model = LogEntry
    template_name = 'logs/index.html'
    paginate_by = 10

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
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crear nuevo elemento')
        return super().form_invalid(form)

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )


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
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


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
        obj = super(borrar_asignacion, self).get_object()
        obj_display = str(obj)
        self.log_deletion(self.request, obj, obj_display)
        return super().delete(request, *args, **kwargs)
    
    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import DELETION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )

#
# CRUD Usuarios
#
decoradores = [login_required(login_url="login"), permission_required('auth.add_user', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_usuarios(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Usuario creado con exito")
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el usuario")
        self.log_addition(self.request, form.instance, 'Error al crear nuevo elemento')
        return super().form_invalid(form)
    
    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )


decoradores = [login_required(login_url="login"), permission_required('auth.change_user', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class editar_usuarios(FormView):
    model = User
    form_class = UsuarioForm
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('editar_usuarios')

    def get(self, request,  *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


decoradores = [login_required(login_url="login")]
@method_decorator(decoradores, name='dispatch')

class editar_perfil(FormView):
    model = User
    form_class = PerfilForm
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('editar_perfil')

    def get(self, request,  *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)
    
    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


decoradores = [login_required(login_url="login")]
@method_decorator(decoradores, name='dispatch')

class cambiar_password(FormView):
    model = User
    form_class = SetPasswordForm
    template_name = 'usuarios/password.html'
    success_url = reverse_lazy('cambiar_password')

    def get(self, request,  *args, **kwargs):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Cambio de contraseña con exito")
        self.log_change(self.request, form.save(), 'Cambio de contraseña')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error en el cambio de contraseña")
        self.log_change(self.request, form.save(), 'Error en cambio de contraseña')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


#
# Tipos de usuario / Grupos [Permisos]
#
decoradores = [login_required(login_url="login"), permission_required('auth.view_user', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class lts_usuarios(ListView):
    model = User
    template_name = 'tipo_usuarios/index.html'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


decoradores = [login_required(login_url="login"), permission_required('auth.add_group', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class crear_grupo(CreateView):
    model = Group
    form_class = GruposForm
    template_name = 'tipo_usuarios/crear_grupos.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento creado con exito")
        self.log_addition(self.request, form.instance, 'Crea nuevo elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al crear el elemento")
        self.log_addition(self.request, form.instance, 'Error al crear nuevo elemento')
        return super().form_invalid(form)

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import ADDITION, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )


decoradores = [login_required(login_url="login"), permission_required('auth.change_user', raise_exception=True)]
@method_decorator(decoradores, name='dispatch')

class actualizar_permisos(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = 'tipo_usuarios/actualizar_permisos.html'
    success_url = reverse_lazy('lts_usuarios')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Elemento actualizado con exito")
        self.log_change(self.request, form.instance, 'Actualiza elemento')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.info(self.request, "Error al actualizar el elemento")
        self.log_change(self.request, form.instance, 'Error al actualizar elemento')
        return super().form_invalid(form)

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        from django.contrib.admin.models import CHANGE, LogEntry
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )


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
