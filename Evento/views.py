from django.shortcuts import render
from .models import Evento, TipoDeEvento
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .forms import criar_evento_form

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


def criar_evento(request):
    submitted = False
    if request.method == "POST":
        form = criar_evento_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Evento/criar_evento?submitted=True')
    else:
        form = criar_evento_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'criar_evento.html', {'form' : form, 'submitted' : submitted})



def cancelar_evento(request, evento_id):
    Evento_view = Evento.objects.get(pk = evento_id)
    Evento_view.delete()
    return redirect('Evento:consultar_eventos_all')

    