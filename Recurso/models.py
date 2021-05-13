from django.db import models


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Campus'

class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.SET_NULL, default=None, null=True, db_column='CampusID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Edificio'

class Equipamento(models.Model):
    recursoid = models.OneToOneField('Recurso', models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    tipo_de_equipamentoid = models.ForeignKey('TipoDeEquipamento', models.DO_NOTHING, db_column='Tipo de equipamentoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Equipamento'

class Recurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Recurso'

class Sala(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    edificioid = models.ForeignKey(Edificio, models.SET_NULL, default=None, null=True, db_column='EdificioID')  # Field name made lowercase.
    lugares = models.IntegerField(db_column='Lugares', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Sala'

class Serviço(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    tipo_de_serviçoid = models.ForeignKey('TipoDeServiço', models.SET_NULL, default=None, null=True, db_column='Tipo de serviçoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Serviço'

class TipoDeEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de equipamento'


class TipoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de recurso'


class TipoDeServiço(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.IntegerField(db_column='Nome', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de serviço'