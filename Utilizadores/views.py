from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, response
from .models import *
from django.contrib import messages
from .form import *



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
        if(Utilizador.objects.filter(username = form.data['username'])):
                error_message = 'This username already exists'
        elif(Utilizador.objects.filter(email = form.data['email'])):
                error_message = 'This email already exists'
        elif form.is_valid():
            
                user = form.save()
                #login(request, user)
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

def login(request):
    if request.method == "POST":
        form = login_form(request.POST)
        if(Utilizador.objects.filter(username = form.data['username'])):
                error_message = 'This username already exists'
        elif(Utilizador.objects.filter(email = form.data['email'])):
                error_message = 'This email already exists'
        elif form.is_valid():
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
