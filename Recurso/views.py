from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def consultar_salas(request):
	return render(request, "consultar_salas.html", {'salas' : Sala.objects.all, 'edificios': Edificio.objects.all()})

def adicionar_salas(request):
    submitted = False
    if request.method == "POST":
        r_form = recursos_form(request.POST)
        s_form = salas_form(request.POST)
        if s_form.is_valid() and r_form.is_valid():
            new_id = r_form.save()
            new_sala = Sala(recursoid = new_id, edificioid = get_object_or_404(Edificio, id = s_form.data['edificioid']), lugares = s_form.data['lugares'])
            new_sala.save()
            return HttpResponseRedirect('/Recurso/consultar_salas?submitted=True')
    else:
        r_form = recursos_form()
        s_form = salas_form()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "adicionar_salas.html", {'s_form':s_form, 'r_form':r_form, 'submitted':submitted})    

def cancelar_salas(request, removeid):
    Sala.objects.get(pk = removeid).delete()
    return redirect('Recurso:consultar_salas')

def omitir_salas(request, omitirid):
    omit = get_object_or_404(Edificio, id = omitirid)
    salas = Sala.objects.filter(edificioid = omit)
    return render(request, "consultar_salas.html", {'salas': salas,
                                                    'edificios': Edificio.objects.all()})

def alterar_salas(request, alterarid):
    sala_change = Sala.objects.get(pk = alterarid)
    recurso_change = Recurso.objects.get(pk = alterarid)
    s_form = salas_form(request.POST or None, instance=sala_change)
    r_form = recursos_form(request.POST or None, instance=recurso_change)
    if s_form.is_valid() and r_form.is_valid():
        r_form.save()
        s_form.save()
        return redirect('Recurso:consultar_salas')
    return render(request, "alterar_sala.html", {'sala_change': sala_change, 'recurso_change': recurso_change, 's_form':s_form, 'r_form':r_form})

#======================================================================================================================================================

def consultar_serviços(request):
	return render(request, "consultar_serviços.html", {'serviços' : Serviço.objects.all, 'tipos': Recurso_estado.objects.all()})

def adicionar_serviços(request):
    submitted = False
    if request.method == "POST":
        r_form = recursos_form(request.POST)
        if r_form.is_valid():
            new_rid = r_form.save()
            new_serviço = Serviço(recursoid = new_rid)
            new_serviço.save()
            return HttpResponseRedirect('/Recurso/consultar_serviços?submitted=True')
    else:
        r_form = recursos_form()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "adicionar_serviços.html", {'r_form':r_form, 'submitted':submitted})

def cancelar_serviços(request, removeid):
    Serviço.objects.get(pk = removeid).delete()
    return redirect('Recurso:consultar_serviços')

def omitir_serviços(request, omitirid):
    omit = get_object_or_404(Recurso_estado, id = omitirid)
    serviços = Serviço.objects.filter(recursoid__estado = omit)
    return render(request, "consultar_serviços.html", {'serviços': serviços,
                                                    'tipos': Recurso_estado.objects.all()})
    
def alterar_serviços(request, alterarid):
    recurso_change = Recurso.objects.get(pk = alterarid)
    r_form = recursos_form(request.POST or None, instance=recurso_change)
    if r_form.is_valid():
        r_form.save()
        return redirect('Recurso:consultar_serviços')
    return render(request, "alterar_serviços.html", {'recurso_change': recurso_change, 'r_form':r_form})

#======================================================================================================================================================

def consultar_equipamentos(request):
	return render(request, "consultar_equipamentos.html", {'equipamentos' : Equipamento.objects.all, 'tipos': Recurso_estado.objects.all()})

def adicionar_equipamentos(request):
    submitted = False
    if request.method == "POST":
        r_form = recursos_form(request.POST)
        if r_form.is_valid():
            new_rid = r_form.save()
            new_serviço = Equipamento(recursoid = new_rid)
            new_serviço.save()
            return HttpResponseRedirect('/Recurso/consultar_equipamentos?submitted=True')
    else:
        r_form = recursos_form()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "adicionar_equipamentos.html", {'r_form':r_form, 'submitted':submitted})

def cancelar_equipamentos(request, removeid):
    Equipamento.objects.get(pk = removeid).delete()
    return redirect('Recurso:consultar_equipamentos')

def omitir_equipamentos(request, omitirid):
    omit = get_object_or_404(Recurso_estado, id = omitirid)
    equipamentos = Equipamento.objects.filter(recursoid__estado = omit)
    return render(request, "consultar_equipamentos.html", {'equipamentos': equipamentos,
                                                            'tipos': Recurso_estado.objects.all()})
    
def alterar_equipamentos(request, alterarid):
    recurso_change = Recurso.objects.get(pk = alterarid)
    r_form = recursos_form(request.POST or None, instance=recurso_change)
    if r_form.is_valid():
        r_form.save()
        return redirect('Recurso:consultar_equipamentos')
    return render(request, "alterar_equipamentos.html", {'recurso_change': recurso_change, 'r_form':r_form})