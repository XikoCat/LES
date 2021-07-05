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
	path("consultar_eventos_all", views.consultar_eventos_all, name="consultar_eventos_all"),
    path("consultar_eventos_proponente_all", views.consultar_eventos_proponente_all, name="consultar_eventos_proponente_all"),
    path("consultar_eventos_validados_all", views.consultar_eventos_validados_all, name="consultar_eventos_validados_all"),
    path("consultar_eventos_proponente/<cat_id>", views.consultar_eventos_proponente, name="consultar_eventos_proponente"),
    path("consultar_eventos_validados/<cat_id>", views.consultar_eventos_validados, name="consultar_eventos_validados"),

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

    path("submeter_logistica/<logistica_id>", views.submeter_logistica, name="submeter_logistica"),
    path("validar_logistica/<logistica_id>", views.validar_logistica, name="validar_logistica"),
    
    path("atribuir_sala/<evento_id>", views.atribuir_sala, name="atribuir_sala"),
    path("atribuir_equipamento/<evento_id>", views.atribuir_equipamento, name="atribuir_equipamento"),
    path("atribuir_serviço/<evento_id>", views.atribuir_serviço, name="atribuir_serviço"),
    
    path("cancelar_atribuir_sala/<removeid>", views.cancelar_atribuiçao_sala, name="cancelar_atribuir_sala"),
    path("cancelar_atribuir_equipamento/<removeid>", views.cancelar_atribuiçao_equipamento, name="cancelar_atribuir_equipamento"),
    path("cancelar_atribuir_serviço/<removeid>", views.cancelar_atribuiçao_serviço, name="cancelar_atribuir_serviço"),
]
