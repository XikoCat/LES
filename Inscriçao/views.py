from django.shortcuts import render
from Pergunta.models import Inscrição

# Create your views here.

def consultar_inscrições(request):
	return render(request, "Inscrição/consultar_inscrições.html", {'Inscrição' : Inscrição.objects.all})