from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar-usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('adicionar-usuario/', views.adicionar_usuario, name='adicionar_usuario'),
    path('visualizar-usuario/<int:usuario_id>/', views.visualizar_usuario, name='visualizar_usuario'),
    path('listar-projetos/', views.listar_projetos, name='listar_projetos'),
    path('visualizar-projeto/<int:projeto_id>/', views.visualizar_projeto, name='visualizar_usuario'),
    path('professor/<int:professor_id>/criar-projeto/', views.criar_projeto, name='criar_projeto'),
    path('projeto/<int:projeto_id>/criar-atividade/', views.criar_atividade, name='criar_atividade'),
    path('projeto/<int:projeto_id>/criar-relatorio/', views.criar_relatorio, name='criar_relatorio'),
    path('visualizar-atividade/<int:atividade_id>/projeto/<int:projeto_id>', views.visualizar_atividade, name='visualizar_atividade'),
    path('atividade/<int:atividade_id>/executar/projeto/<int:projeto_id>/', views.executar_atividade, name='executar_atividade'),
    path('projeto/<int:projeto_id>/finalizar/', views.finalizar_projeto, name='finalizar_projeto'),
    path('aprovar-projeto/<int:projeto_id>/', views.aprovar_projeto, name='aprovar_projeto'),
]
