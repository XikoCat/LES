from django.db.models.deletion import SET_NULL
from Evento.models import Evento
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inscrição
from Evento.models import Evento

# Create your views here.

def consultar_inscrições(request, evento_id):
	evento = SET_NULL
	if evento_id != "all":
		evento = get_object_or_404(Evento, id = evento_id)
	return render(request, "consultar_inscricoes.html", {'Inscrição' : Inscrição.objects.all, 'evento' : evento})


def consultar_inscrições_all(request):
	return redirect('/Inscricao/consultar_inscrições/all')