from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarescola, name='listarescola'),
    path('cadastrarescola/', views.cadastrarescola, name='cadastrarescola'),
    path('cadastrarkit/', views.cadastrarkit, name='cadastrarkit'),
    path('escola/excluir/<int:id>/', views.excluir_escola, name='excluir_escola'),
    path('kit/excluir/<int:id>/', views.excluir_kit, name='excluir_kit'),
path('escola/editar/<int:id>/', views.editar_escola, name='editar_escola'),
    path('kit/editar/<int:id>/', views.editar_kit, name='editar_kit'),
]