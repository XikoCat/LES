from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,            
		)
		user.Estado = 1
		user.TipoUtilizador = 'Administrador'
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Utilizador(AbstractBaseUser):

    class ENUM(models.TextChoices):
        PARTICIPANTE = 'Participante', ('Participante')
        ADMINISTRADOR = 'Administrador', ('Administrador')
        PROPONENTE = 'Proponente', ('Proponente')

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
    TipoUtilizador = models.CharField(max_length=30,choices=ENUM.choices,default=ENUM.PARTICIPANTE,)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

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