from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views, forms
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercade, name='acercade'),
    path('ayuda/', views.ayuda, name='ayuda'),

    path('usuarios/', views.lts_usuarios, name='lts_usuarios'),
    path('usuarios/crear', crear_usuarios.as_view(), name='crear_usuarios'),
    path('usuarios/editar', editar_usuarios.as_view(), name='editar_usuarios'),
    path('usuarios/editar_perfil', editar_perfil.as_view(), name='editar_perfil'),
    path('usuarios/password', cambiar_password.as_view(), name='cambiar_password'),

    path('tipo_usuarios/', lts_usuarios.as_view(), name='lts_usuarios'),
    path('tipo_usuarios/crear', crear_grupo.as_view(), name='crear_grupo'),
    path('tipo_usuarios/<int:pk>/editar', actualizar_permisos.as_view(), name='actualizar_permisos'),

    path('sedes/', lts_sedes.as_view(), name='lts_sedes'),
    path('sedes/<int:pk>/', detalle_sede.as_view(), name='detalle_sede'),
    path('sedes/crear', crear_sede.as_view(), name='crear_sede'),
    path('sedes/<int:pk>/actualizar', actualizar_sede.as_view(), name='actualizar_sede'),
    path('sedes/<int:pk>/borrar', borrar_sede.as_view(), name='borrar_sede'),

    path('ambientes/', lts_ambiente.as_view(), name='lts_ambiente'),
    path('ambientes/<int:pk>/', detalle_ambiente.as_view(), name='detalle_ambiente'),
    path('ambientes/crear', crear_ambiente.as_view(), name='crear_ambiente'),
    path('ambientes/<int:pk>/actualizar', actualizar_ambiente.as_view(), name='actualizar_ambiente'),
    path('ambientes/<int:pk>/borrar', borrar_ambiente.as_view(), name='borrar_ambiente'),

    path('categorias/', lts_categoria.as_view(), name='lts_categoria'),
    path('categorias/<int:pk>/', detalle_categoria.as_view(), name='detalle_categoria'),
    path('categorias/crear', crear_categoria.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/actualizar', actualizar_categoria.as_view(), name='actualizar_categoria'),
    path('categorias/<int:pk>/borrar', borrar_categoria.as_view(), name='borrar_categoria'),

    path('activos/', lts_activo.as_view(), name='lts_activo'),
    path('activos/<int:pk>/', detalle_activo.as_view(), name='detalle_activo'),
    path('activos/crear', crear_activo.as_view(), name='crear_activo'),
    path('activos/<int:pk>/actualizar', actualizar_activo.as_view(), name='actualizar_activo'),
    path('activos/<int:pk>/borrar', borrar_activo.as_view(), name='borrar_activo'),

    path('asignaciones/', lts_asignacion.as_view(), name='lts_asignacion'),
    path('asignaciones/<int:pk>/', detalle_asignacion.as_view(), name='detalle_asignacion'),
    path('asignaciones/crear', crear_asignacion.as_view(), name='crear_asignacion'),
    path('asignaciones/<int:pk>/actualizar', actualizar_asignacion.as_view(), name='actualizar_asignacion'),
    path('asignaciones/<int:pk>/borrar', borrar_asignacion.as_view(), name='borrar_asignacion'),

    path('consultas/', views.lts_consulta, name='lts_consulta'),
    path('consultas/filtrada', filtrar_consulta.as_view(), name='filtrar_consulta'),
    path('consultas/<int:_id>/', views.detalle_consulta, name='detalle_consulta'),
    path('consultas/exportar', views.exportar_asignacion, name='exportar_asignacion'),

    path('login/', iniciar_sesion.as_view(), name="login"),
    path('logout', cerrar_sesion.as_view(), name='logout'),

    path('historial/', historial.as_view(), name='historial'),
    path('ayuda/1', views.manual_operaciones, name='manual_operaciones'),
    path('ayuda/2', views.manual_usuario, name='manual_usuario'),
]
