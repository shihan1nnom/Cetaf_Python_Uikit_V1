from django.urls import path, re_path

from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercade, name='acercade'),
    path('ayuda/', views.ayuda, name='ayuda'),

    path('usuarios/', views.lts_usuarios, name='lts_usuarios'),
    path('usuarios/crear', views.crear_usuarios, name='crear_usuarios'),
    path('usuarios/editar', views.editar_usuarios, name='editar_usuarios'),
    path('usuarios/editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('usuarios/password', views.cambiar_password, name='cambiar_password'),

    path('tipo_usuarios/', views.lts_usuarios, name='lts_usuarios'),
    path('tipo_usuarios/crear', views.crear_grupo, name='crear_grupo'),
    path('tipo_usuarios/<int:_id>/editar', views.actualizar_permisos, name='actualizar_permisos'),

    path('sedes/', views.lts_sedes, name='lts_sedes'),
    path('sedes/<int:_id>/', views.detalle_sede, name='detalle_sede'),
    path('sedes/crear', views.crear_sede, name='crear_sede'),
    path('sedes/<int:_id>/actualizar', views.actualizar_sede, name='actualizar_sede'),
    path('sedes/<int:_id>/borrar', views.borrar_sede, name='borrar_sede'),

    path('ambientes/', views.lts_ambiente, name='lts_ambiente'),
    path('ambientes/<int:_id>/', views.detalle_ambiente, name='detalle_ambiente'),
    path('ambientes/crear', views.crear_ambiente, name='crear_ambiente'),
    path('ambientes/<int:_id>/actualizar', views.actualizar_ambiente, name='actualizar_ambiente'),
    path('ambientes/<int:_id>/borrar', views.borrar_ambiente, name='borrar_ambiente'),

    path('categorias/', views.lts_categoria, name='lts_categoria'),
    path('categorias/<int:_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('categorias/crear', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:_id>/actualizar', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/<int:_id>/borrar', views.borrar_categoria, name='borrar_categoria'),

    path('activos/', views.lts_activo, name='lts_activo'),
    path('activos/<int:_id>/', views.detalle_activo, name='detalle_activo'),
    path('activos/crear', views.crear_activo, name='crear_activo'),
    path('activos/<int:_id>/actualizar', views.actualizar_activo, name='actualizar_activo'),
    path('activos/<int:_id>/borrar', views.borrar_activo, name='borrar_activo'),

    path('asignaciones/', views.lts_asignacion, name='lts_asignacion'),
    path('asignaciones/<int:_id>/', views.detalle_asignacion, name='detalle_asignacion'),
    path('asignaciones/crear', views.crear_asignacion, name='crear_asignacion'),
    path('asignaciones/<int:_id>/actualizar', views.actualizar_asignacion, name='actualizar_asignacion'),
    path('asignaciones/<int:_id>/borrar', views.borrar_asignacion, name='borrar_asignacion'),

    path('consultas/', views.lts_consulta, name='lts_consulta'),
    path('consultas/filtrada', views.filtrar_consulta, name='filtrar_consulta'),
    path('consultas/<int:_id>/', views.detalle_consulta, name='detalle_consulta'),

    path('login/', views.iniciar_sesion, name="login"),
    path('logout', views.cerrar_sesion, name='logout'),
]
