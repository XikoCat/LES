from django.shortcuts import render
from Pergunta.models import Pergunta

# Create your views here.

def consultar_perguntas(request):
	return render(request, "consultar_perguntas.html", {'Pergunta' : Pergunta.objects.all})