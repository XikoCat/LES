"""LES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
app_name = "Formulario"

urlpatterns = [
    path("consultar_perguntas/<id>/<formulario_id>", views.consultar_perguntas, name="consultar_perguntas"),
    path("add_pergunta/<formulario_id>", views.add_pergunta, name="add_pergunta"),
    path("add_opcao_resposta/<pergunta_id>/<formulario_id>", views.add_opcao_resposta, name="add_opcao_resposta"),
    path("remover_perguntas/<pergunta_id>/<formulario_id>", views.remover_pergunta, name="remover_pergunta"),
    path("delete_resposta/<pergunta_id>/<resposta_id>/<formulario_id>", views.delete_resposta, name="delete_resposta"),
    path("editar_pergunta/<pergunta_id>/<formulario_id>", views.editar_pergunta, name="editar_pergunta"),
    path("editar_opcao_resposta/<pergunta_id>/<resposta_id>/<formulario_id>", views.editar_opcao_resposta, name="editar_opcao_resposta"),
    
    path("consultar_formularios/<evento_id>", views.consultar_formularios, name="consultar_formularios"),
    
    path("add_formulario/<evento_id>", views.add_formulario, name="add_formulario"),
    path("add_pergunta_ao_formulario/<formulario_id>", views.add_pergunta_ao_formulario, name="add_pergunta_ao_formulario"),
    path("editar_formulario/<formulario_id>", views.editar_formulario, name="editar_formulario"),
    path("eliminar_formulario/<formulario_id>", views.eliminar_formulario, name="eliminar_formulario"),
    path("alterar_estado_formulario/<formulario_id>", views.alterar_estado_formulario, name="alterar_estado_formulario"),
    path("add_pergunta_ao_formulario_action/<pergunta_id>/<formulario_id>", views.add_pergunta_ao_formulario_action, name="add_pergunta_ao_formulario_action"),

    path("remover_pergunta_do_formulario/<pergunta_id>/<formulario_id>", views.remover_pergunta_do_formulario, name="remover_pergunta_do_formulario"),
    path("editar_pergunta_do_formulario/<pergunta_id>/<formulario_id>", views.editar_pergunta_do_formulario, name="editar_pergunta_do_formulario"),
    
]
