from django.db import models


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', unique=True, max_length=255, blank=True, null=True) 
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Campus'

class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    campusid = models.ForeignKey(Campus, models.SET_NULL, default=None, null=True, db_column='CampusID') 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Edificio'

class Equipamento(models.Model):
    recursoid = models.OneToOneField('Recurso', models.DO_NOTHING, db_column='RecursoID', primary_key=True) 
    tipo_de_equipamentoid = models.ForeignKey('TipoDeEquipamento', models.DO_NOTHING, db_column='Tipo de equipamentoID') 

    class Meta:
        managed = True
        db_table = 'Equipamento'

class Recurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Recurso'

class Sala(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True) 
    edificioid = models.ForeignKey(Edificio, models.SET_NULL, default=None, null=True, db_column='EdificioID') 
    lugares = models.IntegerField(db_column='Lugares', blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Sala'

class Serviço(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True) 
    tipo_de_serviçoid = models.ForeignKey('TipoDeServiço', models.SET_NULL, default=None, null=True, db_column='Tipo de serviçoID') 

    class Meta:
        managed = True
        db_table = 'Serviço'

class TipoDeEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Tipo de equipamento'


class TipoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Tipo de recurso'


class TipoDeServiço(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True) 

    class Meta:
        managed = True
        db_table = 'Tipo de serviço'