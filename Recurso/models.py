from django.db import models


class Campus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nome)

    class Meta:
        managed = True
        db_table = 'Campus'

class Edificio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campusid = models.ForeignKey(Campus, models.SET_NULL, verbose_name='Campus', default=None, null=True, db_column='CampusID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', verbose_name='Edificio', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nome)
    
    class Meta:
        managed = True
        db_table = 'Edificio'

class Equipamento(models.Model):
    recursoid = models.OneToOneField('Recurso', models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.recursoid.nome)

    class Meta:
        managed = True
        db_table = 'Equipamento'

class Recurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 
    estado = models.ForeignKey('Recurso_estado', models.DO_NOTHING, default=None, null=False, db_column='Estado')

    def __str__(self):
        return str(self.nome)

    class Meta:
        managed = True
        db_table = 'Recurso'

class Recurso_estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    Estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True) 

    def __str__(self):
        return str(self.Estado)

    class Meta:
        managed = True
        db_table = 'Recurso_estado'

class Sala(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, verbose_name='Sala', db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    edificioid = models.ForeignKey(Edificio, models.SET_NULL, verbose_name='Edificio', default=None, null=True, db_column='EdificioID')  # Field name made lowercase.
    lugares = models.IntegerField(db_column='Lugares', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.recursoid)

    class Meta:
        managed = True
        db_table = 'Sala'

class Serviço(models.Model):
    recursoid = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='RecursoID', primary_key=True)  # Field name made lowercase.
    
    def __str__(self):
        return str(self.recursoid.nome)

    class Meta:
        managed = True
        db_table = 'Serviço'

class TipoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True,max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo de recurso'