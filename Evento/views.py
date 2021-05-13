from django.shortcuts import render
from .models import Evento, TipoDeEvento
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.

def consultar_eventos(request, cat_id):
    categories = TipoDeEvento.objects.all()
    category = get_object_or_404(TipoDeEvento, id = cat_id)
    Eventos = Evento.objects.filter(tipo_de_eventoid = category)
    return render(request, 'consultar_eventos.html', {'Eventos' : Eventos,
                                                      'TipoDeEvento' : categories})

def consultar_eventos_all(request):
    categories = TipoDeEvento.objects.all()
    Eventos = Evento.objects.all()
    return render(request, 'consultar_eventos.html', {'Eventos' : Eventos,
                                                      'TipoDeEvento' : categories})

def visualizar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    return render(request, 'visualizar_evento.html', {'Evento' : Evento_view})



def cancelar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_view.delete()
    return HttpResponseRedirect("consultar_eventos")

    