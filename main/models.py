# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizadores.Utilizador', models.SET_NULL, default=None, null=True, db_column='UtilizadorID')  # Field name made lowercase.
    remetente = models.CharField(db_column='Remetente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    receptor = models.CharField(db_column='Receptor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conteúdo = models.CharField(db_column='Conteúdo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Mensagem'


class UtilizadorMensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizadores.Utilizador', models.SET_NULL, default=None, null=True, db_column='UtilizadorID')  # Field name made lowercase.
    mensagemid = models.ForeignKey('Mensagem', models.SET_NULL, default=None, null=True, db_column='MensagemID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Utilizador_Mensagem'
