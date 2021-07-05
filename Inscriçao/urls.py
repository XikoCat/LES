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

app_name = "Inscriçao"

urlpatterns = [
    # DEFAULT PATH
    path("", views.consultar_inscricoes_all, name="consultar_inscricoes"),
       
    # Consultar inscrições
    path(
        "consultar_user/<user_id>",
        views.consultar_inscricoes_user,
        name="consultar_inscricoes_user",
    ),
    path(
        "consultar_evento/<evento_id>",
        views.consultar_inscricoes_evento,
        name="consultar_inscricoes_evento",
    ),
    path(
        "consultar_all",
        views.consultar_inscricoes_all,
        name="consultar_inscricoes_all",
    ),

    # Consultar inscrição
    path(
        "consultar/<inscricao_id>",
        views.consultar,
        name="consultar",
    ),
    # Editar inscrição
    path(
        "editar/<inscricao_id>",
        views.editar,
        name="editar",
    ),
    # Criar Inscrição
    path(
        "criar/<evento_id>",
        views.criar,
        name="criar",
    ),
    # Remover Inscrição
    path(
        "remover/<inscricao_id>",
        views.remover,
        name="remover",
    ),
    # Validar Inscrição
    path(
        "validar/<inscricao_id>",
        views.validar,
        name="validar",
    ),
    # Checkin Inscrição
    path(
        "checkin",
        views.checkin,
        name="checkin",
    ),

]
