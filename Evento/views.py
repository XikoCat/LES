from django.shortcuts import render
from .models import Evento, TipoDeEvento, PedidoDeRecurso
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from Recurso.models import *

# Create your views here.

def consultar_eventos(request, cat_id):
    categories = TipoDeEvento.objects.all()
    category = get_object_or_404(TipoDeEvento, id = cat_id)
    Eventos = Evento.objects.filter(tipo_de_eventoid = category)
    Logisticas = PedidoDeRecurso.objects.all()
    return render(request, 'consultar_eventos.html', {'Eventos' : Eventos,
                                                      'Logisticas' : Logisticas,
                                                      'TipoDeEvento' : categories})

def consultar_eventos_all(request):
    categories = TipoDeEvento.objects.all()
    Eventos = Evento.objects.all()
    return render(request, 'consultar_eventos.html', {'Eventos' : Eventos,
                                                      'TipoDeEvento' : categories})

def visualizar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_Equipamentos_view = EventoEquipamentos.objects.filter(eventoId = evento_id)
    Evento_Local_view = EventoLocais.objects.filter(eventoId = evento_id)
    Evento_Servicos_view = EventoServicos.objects.filter(eventoId = evento_id)
    return render(request, 'visualizar_evento.html', {'Evento' : Evento_view, 'Equipamento' : Evento_Equipamentos_view,
                                                      'Servico' : Evento_Servicos_view, 'Local' : Evento_Local_view})


def criar_evento(request):
    submitted = False
    if request.method == "POST":
        form = evento_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Evento/criar_evento?submitted=True')
    else:
        form = evento_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'criar_evento.html', {'form' : form, 'submitted' : submitted})


def cancelar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_view.delete()
    return redirect('Evento:consultar_eventos_all')


def editar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    form = evento_form(request.POST or None, instance = Evento_view)
    if form.is_valid():
        form.save()
        return redirect('Evento:consultar_eventos_all')
    return render(request, 'editar_evento.html', {'Evento' : Evento_view, 
                                                  'form' : form})
                                                  

def submeter_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_view.estado='Submetido'
    Evento_view.save()
    return redirect('Evento:consultar_eventos_all')

def validar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_view.estado='Validado'
    Evento_view.save()
    return redirect('Evento:consultar_eventos_all')


def criar_logistica(request):
    submitted = False
    if request.method == "POST":
        form = logistica_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Evento/criar_logistica?submitted=True')
    else:
        form = logistica_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'criar_logistica.html', {'form' : form, 'submitted' : submitted})


def visualizar_logistica(request, evento_id):
    Logistica_view = PedidoDeRecurso.objects.filter(eventoid = evento_id)
    Evento_view = Evento.objects.get(pk = evento_id)
    return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica_view, 'Evento' : Evento_view})


def editar_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)

    Logistica = PedidoDeRecurso.objects.filter(eventoid = Logistica_view.eventoid)
    Evento_view = Evento.objects.get(pk = Logistica_view.eventoid.id)

    form = logistica_form(request.POST or None, instance = Logistica_view)
    if form.is_valid():
        form.save()
        return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica, 'Evento' : Evento_view})

    return render(request, 'editar_logistica.html', {'Logistica' : Logistica_view, 
                                                  'form' : form})

def cancelar_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)

    Logistica = PedidoDeRecurso.objects.filter(eventoid = Logistica_view.eventoid)
    Evento_view = Evento.objects.get(pk = Logistica_view.eventoid.id)

    Logistica_view.delete()
    return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica, 'Evento' : Evento_view})

def submeter_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)

    Logistica = PedidoDeRecurso.objects.filter(eventoid = Logistica_view.eventoid)
    Evento_view = Evento.objects.get(pk = Logistica_view.eventoid.id)

    Logistica_view.estado='Submetido'
    Logistica_view.save()
    return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica, 'Evento' : Evento_view})

def validar_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)

    Logistica = PedidoDeRecurso.objects.filter(eventoid = Logistica_view.eventoid)
    Evento_view = Evento.objects.get(pk = Logistica_view.eventoid.id)

    Logistica_view.estado='Validado'
    Logistica_view.save()
    return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica, 'Evento' : Evento_view})

#===================================Atribuições=======================================

def atribuir_sala(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    if request.method == "POST":
        form = atribuir_sala_form(request.POST)
        if form.is_valid():
            EventoLocais(eventoId = Evento_view, localId = get_object_or_404(Sala, recursoid = form.data['localId'])).save()
            return redirect('Evento:consultar_eventos_all')
    else:
        form = atribuir_sala_form()
    return render(request, 'atribuir_sala.html', {'form' : form})

def atribuir_equipamento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    if request.method == "POST":
        form = atribuir_equipamento_form(request.POST)
        if form.is_valid():
            EventoEquipamentos(eventoId = Evento_view, equipamentoId = get_object_or_404(Equipamento, recursoid = form.data['equipamentoId'])).save()
            return redirect('Evento:consultar_eventos_all')
    else:
        form = atribuir_equipamento_form()
    return render(request, 'atribuir_equipamento.html', {'form' : form})

def atribuir_serviço(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    if request.method == "POST":
        form = atribuir_serviço_form(request.POST)
        if form.is_valid():
            EventoServicos(eventoId = Evento_view, servicoId = get_object_or_404(Serviço, recursoid = form.data['servicoId'])).save()
            return redirect('Evento:consultar_eventos_all')
    else:
        form = atribuir_serviço_form()
    return render(request, 'atribuir_serviço.html', {'form' : form})

def cancelar_atribuiçao_sala(request, removeid):
    EventoLocais.objects.all().filter(eventoId = Evento.objects.get(pk = removeid)).delete()
    return redirect('Evento:consultar_eventos_all')

def cancelar_atribuiçao_equipamento(request, removeid):
    EventoEquipamentos.objects.all().filter(eventoId = Evento.objects.get(pk = removeid)).delete()
    return redirect('Evento:consultar_eventos_all')

def cancelar_atribuiçao_serviço(request, removeid):
    EventoServicos.objects.all().filter(eventoId = Evento.objects.get(pk = removeid)).delete()
    return redirect('Evento:consultar_eventos_all')
    