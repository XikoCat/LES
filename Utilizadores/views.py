from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from django.contrib import messages
from .form import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password, check_password




def consultar_utilizadores(request):
	return render(
        request,
        "consultar_utilizadores.html",
        {
            "utilizadores": Utilizador.objects.all()
        },
    )

def register(request):
    if request.method == "POST":
        form = user_form(request.POST)
        error_message = None
        if(Utilizador.objects.filter(username = form.data['username'])):
            error_message = 'Este username já existe'
        elif(Utilizador.objects.filter(email = form.data['email'])):
            error_message = 'Este email já existe'
        elif form.is_valid():
            user = form.save()
            user.password=make_password(user.password)
            user.save()
            Participante(utilizadorid = user).save()
            Proponente(utilizadorid = user).save()
            login(request, user)
            return redirect("/")
        return render(
            request,
            "register.html",
            {
                "form": form, "error_message": error_message
            },
        )
    else:
        form = user_form
    return render(
        request,
        "register.html",
        {
            "form": form
        },
    )

def login_action(request):

    if request.method == "POST":
        form = login_form(request.POST)
        utilizador = Utilizador.objects.filter(username = form.data['username'])
        error_message = None
        if(not utilizador):
            error_message = 'Este username não existe'
        elif not check_password(form.data['password'], utilizador[0].password):
            error_message = 'A password inserida é incorreta'
        else:
            user = authenticate(username=form.data['username'], password= form.data['password'])
            if user is not None:
                login(request, user)
            return redirect("/")
        return render(
            request,
            "login.html",
            {
                "form": form, "error_message": error_message
            },
        )
    else:
        form = login_form
    return render(
        request,
        "login.html",
        {
            "form": form
        },
    )

def logout_action(request):
    logout(request)
    return redirect("/")
