from django.urls import path

from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercade, name='acercade'),
    path('ayuda/', views.ayuda, name='ayuda'),

    path('usuarios/', views.lts_usuarios, name='lts_usuarios'),

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
]