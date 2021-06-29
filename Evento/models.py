from Recurso.models import Equipamento
from django.db import models

 

class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    tipo_de_eventoid = models.ForeignKey('TipoDeEvento', models.SET_NULL, default=None, null=True, db_column='Tipo de eventoID')      
    proponenteutilizadorid = models.ForeignKey('main.Proponente', models.SET_NULL, default=None, null=True, db_column='ProponenteUtilizadorID')   
    formulárioinscriçãoid = models.ForeignKey('Formulario.Formulário', models.SET_NULL, default=None, null=True, db_column='FormulárioInscriçãoID')   
    formuláriofeedbackid = models.ForeignKey('Formulario.Formulário', models.SET_NULL, default=None, null=True, related_name = 'feedback', db_column='FormulárioFeedbackID')   
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)   
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, default="Não submetido" , null=True)   
    descrição = models.CharField(db_column='Descrição', max_length=255, blank=True, null=True)   
    data = models.DateField(db_column='Data', blank=True, null=True)   
    hora = models.TimeField(db_column='Hora', blank=True, null=True)   
    duração = models.IntegerField(db_column='Duração', blank=True, null=True)   
    
    locais = models.ForeignKey('EventoLocais', models.SET_NULL, default=None, null=True, db_column='locais')
    equipamentos = models.ForeignKey('EventoEquipamentos', models.SET_NULL, default=None, null=True, db_column='equipamentos')
    servicos = models.ForeignKey('EventoServicos', models.SET_NULL, default=None, null=True, db_column='servicos')

    valor = models.FloatField(db_column='Valor')   
    evento_pagoid = models.IntegerField(db_column='Evento pagoID')      

    def __str__(self):
        return self.nome
        
    class Meta:
        managed = True
        db_table = 'Evento'


class EventoLocais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    eventoId = models.ForeignKey('Evento', models.SET_NULL, null=True, db_column='Evento')
    localId = models.ForeignKey('Recurso.Sala', models.SET_NULL, null=True, db_column='Local')


class EventoEquipamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    eventoId = models.ForeignKey('Evento', models.SET_NULL, null=True, db_column='Evento')
    equipamentoId = models.ForeignKey('Recurso.Equipamento', models.SET_NULL, null=True, db_column='Equipamento')


class EventoServicos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    eventoId = models.ForeignKey('Evento', models.SET_NULL, null=True, db_column='Evento')
    servicoId = models.ForeignKey('Recurso.Serviço', models.SET_NULL, null=True, db_column='Servico')


class CertificadoDeParticipação(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    #eventoid = models.ForeignKey('Evento', models.SET_NULL, default=None, null=True, db_column='EventoID')   
    nome_evento = models.CharField(db_column='Nome evento', max_length=255, blank=True, null=True)      
    data_emissão = models.DateField(db_column='Data emissão', blank=True, null=True)      
    nome_participante = models.CharField(db_column='Nome participante', max_length=255, blank=True, null=True)      
    publico = models.IntegerField(db_column='Publico')   


    class Meta:
        managed = True
        db_table = 'Certificado de Participação'

        
class PedidoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    eventoid = models.ForeignKey(Evento, models.SET_NULL, default=None, null=True, db_column='EventoID')   
    tipo_de_recursoid = models.ForeignKey('Recurso.TipoDeRecurso', models.SET_NULL, default=None, null=True, db_column='Tipo de recursoID')      
    quantidade = models.IntegerField(db_column='Quantidade')   
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)      
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)      
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)      
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)      
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)   
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, default="Não submetido" , null=True)

    class Meta:
        managed = True
        db_table = 'Pedido de recurso'

class Requisição(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    eventoid = models.OneToOneField('Evento.Evento', models.SET_NULL, default=None, null=True, db_column='EventoID')   
    recursoid = models.OneToOneField('Recurso.Recurso', models.SET_NULL, default=None, null=True, db_column='RecursoID')   
    dia_inicial = models.DateField(db_column='Dia inicial', blank=True, null=True)      
    hora_inicial = models.TimeField(db_column='Hora inicial', blank=True, null=True)      
    dia_final = models.DateField(db_column='Dia final', blank=True, null=True)      
    hora_final = models.TimeField(db_column='Hora final', blank=True, null=True)      

    class Meta:
        managed = True
        db_table = 'Requisição'



class TipoDeEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)   

    def __str__(self):
        return self.nome
        
    class Meta:
        managed = True
        db_table = 'Tipo de evento'



    
