from django.db.models.deletion import SET_NULL
from django.shortcuts import render, get_object_or_404, redirect

from .models import Inscrição, Pagamento
from Evento.models import Evento

# Create your views here.

# Visualizar incrição de utilizadores no evento
def consultar_inscricoes(request, evento_id):
    evento = SET_NULL
    if evento_id != "all":
        evento = get_object_or_404(Evento, id=evento_id)
    return render(
        request,
        "consultar_inscricoes.html",
        {
            "Inscrição": Inscrição.objects.all,
            "evento": evento,
            "Dividas": Pagamento.objects.all,
        },
    )


# Visualizar todas as inscrições en todos os eventos
def consultar_inscricoes_all(request):
    return redirect("/Inscricao/consultar_inscricoes/all")


# Visualizar formulario de inscrição
def info_inscricoes(request, evento_id):

    evento = get_object_or_404(Evento, id=evento_id)
    
    # Obter formulário de Inscrição para o evento 'evento_id'

    return render(
        request,
        "info_inscricoes.html",
        {
            "evento": evento,
        },
    )
