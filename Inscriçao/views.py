from django.shortcuts import render
from .models import Inscrição

# Create your views here.

def consultar_inscrições(request):
	return render(request, "consultar_inscrições.html", {'Inscrição' : Inscrição.objects.all})