from django.shortcuts import render
from .models import Sala

def consultar_salas(request):
	return render(request, "consultar_salas.html", {'Sala' : Sala.objects.all})
