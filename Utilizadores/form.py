from django import forms
from django.forms import ModelForm, fields, widgets
from .models import *
from django.contrib import messages


class user_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Utilizador
        fields = (
            'nome',
            'username',
            'email',
            'telefone',
            'password',
        )

class login_form(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Utilizador
        fields = (
            'username',
            'password',
        )

    