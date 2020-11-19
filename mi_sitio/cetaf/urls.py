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
]