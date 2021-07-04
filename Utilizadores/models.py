from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

class Utilizador(AbstractBaseUser):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)
    telefone = models.IntegerField(default="0")
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Utilizadores"
        db_table = "utilizador"

    def __str__(self):
        return self.username 

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

#class Utilizador(User):
#    #id = models.AutoField(db_column='ID', primary_key=True) 
#    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True) 
#    #email = models.CharField(db_column='Email', max_length=255, blank=False, null=True, unique=True) 
#    telefone = models.CharField(db_column='Telefone', max_length=255, blank=True, null=True)  
#    #username = models.CharField(db_column='Username', max_length=255, blank=False, null=True, unique=True)
#    #password = models.CharField(db_column='Password', max_length=255, blank=False, null=True)
#
#    class Meta:
#        managed = True
#        db_table = 'Utilizador'
#    
#    def __str__(self):
#        return str(self.nome)


class Administrador(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True) 

    class Meta:
        managed = True
        db_table = 'Administrador'
    
    def __str__(self):
        return str(self.utilizadorid)

class Participante(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True) 

    class Meta:
        managed = True
        db_table = 'Participante'
    
    def __str__(self):
        return str(self.utilizadorid)


class Proponente(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True) 

    class Meta:
        managed = True
        db_table = 'Proponente'
    
    def __str__(self):
        return str(self.utilizadorid)