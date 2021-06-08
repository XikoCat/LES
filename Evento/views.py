from django.shortcuts import render
from .models import Evento, TipoDeEvento, PedidoDeRecurso
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import evento_form, logistica_form

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
    return render(request, 'visualizar_evento.html', {'Evento' : Evento_view})


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
    return render(request, 'visualizar_logistica.html', {'Logistica' : Logistica_view})


def editar_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)
    form = logistica_form(request.POST or None, instance = Logistica_view)
    if form.is_valid():
        form.save()
        return redirect('Evento:consultar_eventos_all')

    return render(request, 'editar_logistica.html', {'Logistica' : Logistica_view, 
                                                  'form' : form})

def cancelar_logistica(request, logistica_id):
    Logistica_view = PedidoDeRecurso.objects.get(pk = logistica_id)
    Logistica_view.delete()
    return redirect('Evento:consultar_eventos_all')
    