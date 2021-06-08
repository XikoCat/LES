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
app_name = "Recurso"

urlpatterns = [
        path("consultar_salas", views.consultar_salas, name="consultar_salas"),
        path("adicionar_salas", views.adicionar_salas, name="adicionar_salas_view"),
        path("cancelar_salas/<removeid>", views.cancelar_salas, name="remover_salas_view"),
        path("omitir_salas/<omitirid>", views.omitir_salas, name="omitir_salas_view"),
        path("alterar_salas/<alterarid>", views.alterar_salas, name="alterar_salas_view"),
        #=================================================================================
        path("consultar_serviços", views.consultar_serviços, name="consultar_serviços"),
        path("adicionar_serviços", views.adicionar_serviços, name="adicionar_serviços_view"),
        path("cancelar_serviços/<removeid>", views.cancelar_serviços, name="remover_serviços_view"),
        path("omitir_serviços/<omitirid>", views.omitir_serviços, name="omitir_serviços_view"),
        path("alterar_serviços/<alterarid>", views.alterar_serviços, name="alterar_serviços_view"),
        #=================================================================================
        path("consultar_equipamentos", views.consultar_equipamentos, name="consultar_equipamentos"),
        path("adicionar_equipamentos", views.adicionar_equipamentos, name="adicionar_equipamentos_view"),
        path("cancelar_equipamentos/<removeid>", views.cancelar_equipamentos, name="remover_equipamentos_view"),
        path("omitir_equipamentos/<omitirid>", views.omitir_equipamentos, name="omitir_equipamentos_view"),
        path("alterar_equipamentos/<alterarid>", views.alterar_equipamentos, name="alterar_equipamentos_view"),
]

