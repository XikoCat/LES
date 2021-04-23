from django.db import models
from mains.models import Proponente
from Formulario.models import Formul�rio
from Recurso.models import TipoDeFormul�rio, TipoDeEquipamento, TipoDeRecurso, Recurso



class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.SET_NULL, default=None, null=True, db_column='Tipo de eventoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proponenteutilizadorid = models.ForeignKey('Proponente', models.SET_NULL, default=None, null=True, db_column='ProponenteUtilizadorID')  # Field name made lowercase.
    formulárioinscriçãoid = models.ForeignKey('Formulário', models.SET_NULL, default=None, null=True, db_column='FormulárioInscriçãoID')  # Field name made lowercase.
    formuláriofeedbackid = models.ForeignKey('Formulário', models.SET_NULL, default=None, null=True, related_name = 'feedback', db_column='FormulárioFeedbackID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    duração = models.IntegerField(db_column='Duração', blank=True, null=True)  # Field name made lowercase.
    local = models.IntegerField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor')  # Field name made lowercase.
    evento_pagoid = models.IntegerField(db_column='Evento pagoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Evento'


class CertificadoDeParticipação(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey('Evento', models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    nome_evento = models.CharField(db_column='Nome evento', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_emissão = models.DateField(db_column='Data emissão', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome_participante = models.CharField(db_column='Nome participante', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publico = models.IntegerField(db_column='Publico')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Certificado de Participação'

        
class PedidoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    tipo_de_recursoid = models.ForeignKey('TipoDeRecurso', models.SET_NULL, default=None, null=True, db_column='Tipo de recursoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.
    tipo_de_equipamentoid = models.ForeignKey('TipoDeEquipamento', models.SET_NULL, default=None, null=True, db_column='Tipo de equipamentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_serviçoid = models.ForeignKey('TipoDeServiço', models.SET_NULL, default=None, null=True, db_column='Tipo de serviçoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Pedido de recurso'

class Requisição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.OneToOneField(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')  # Field name made lowercase.
    recursoid = models.OneToOneField(Recurso, models.SET_NULL, default=None, null=True, db_column='RecursoID')  # Field name made lowercase.
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Requisição'



    class TipoDeEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de evento'



    
