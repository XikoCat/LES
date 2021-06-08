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
from .import views


app_name = "Evento"

urlpatterns = [
	path("consultar_eventos/<cat_id>", views.consultar_eventos, name="consultar_eventos"),
	path("consultar_eventos", views.consultar_eventos_all, name="consultar_eventos_all"),

	path("visualizar_evento/<evento_id>", views.visualizar_evento, name="visualizar_evento"),

    path("criar_evento", views.criar_evento, name="criar_evento"),

	path("cancelar_evento/<evento_id>", views.cancelar_evento, name="cancelar_evento"),

	path("editar_evento/<evento_id>", views.editar_evento, name="editar_evento"),

    path("submeter_evento/<evento_id>", views.submeter_evento, name="submeter_evento"),
    path("validar_evento/<evento_id>", views.validar_evento, name="validar_evento"),

    path("criar_logistica", views.criar_logistica, name="criar_logistica"),

    path("visualizar_logistica/<evento_id>", views.visualizar_logistica, name="visualizar_logistica"),

    path("editar_logistica/<logistica_id>", views.editar_logistica, name="editar_logistica"),

    path("cancelar_logistica/<logistica_id>", views.cancelar_logistica, name="cancelar_logistica"),
]
