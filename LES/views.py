from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404



def home(request):
    ''' Pagina principal da plataforma '''
    tipo_de_utilizador = ""
    #if request.user.is_authenticated:    
    #    user = get_user(request)
    #    if user.groups.filter(name = "Coordenador").exists():
    #        u = "Coordenador"
    #    elif user.groups.filter(name = "Administrador").exists():
    #        u = "Administrador"
    #    elif user.groups.filter(name = "ProfessorUniversitario").exists():
    #        u = "ProfessorUniversitario"
    #    elif user.groups.filter(name = "Colaborador").exists():
    #        u = "Colaborador"
    #    elif user.groups.filter(name = "Participante").exists():
    #        u = "Participante" 
    #    else:
    #        u=""     
    #else:
    #    u=""
    
    return render(request, "inicio.html",context={ 'tipo_de_utilizador': tipo_de_utilizador})