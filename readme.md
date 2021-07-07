# Gestão de Eventos - Grupo 4

## Instalação

No diretório root do projeto,

### Criar um virtual enviroment

```bash
python3 -m virtualenv .venv
```

### Entrar no virtual enviroment:

```bash
source .venv/bin/activate
```

### Instalar as bibliotecas necessárias no virtual enviroment:

```bash
make install
```

Importar o ficheiro `LES.sql` com o phpmyadmin ou diretamente no MySQL para criar a base de dados

Gerar uma nova SECRET_KEY aleatória (https://djecrety.ir/) e substituí-la no `.env`

### Fazer as migrações necessárias do django

```bash
make migrate
```

## Correr a aplicação

### Localmente

```bash
make run
```

### Apache

Instalar Apache2 e mod_wsgi

Editar o ficheiro httpd:\
(Este é um exemplo onde o root do projeto está localizado no dir `/home/`)

```conf
Listen 8001
WSGIPythonHome /home/LES/.venv
WSGIPythonPath /home/LES

<VirtualHost *:8001>
ServerName django.les

Alias /static/ /home/LES/static/
Alias /templates/ /home/LES/templates

<Directory /home/LES/static>
Require all granted
</Directory>

<Directory /home/LES/templates>
Require all granted
</Directory>

WSGIScriptAlias / /home/LES/LES/wsgi.py
<Directory /home/LES/LES>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
ErrorLog /etc/httpd/apache.error.log
CustomLog /etc/httpd/apache.custom.log common
</VirtualHost>

LoadModule wsgi_module modules/mod_wsgi.so
```

### Dar permissão para o apache ler e executar os ficheiros

```bash
sudo chmod ugo+rwx <dir/do/root/do/projeto>
```

### Reiniciar o serviço apache

```bash
sudo systemclt reload httpd
```

ou, se não estiver iniciado:

```bash
sudo systemclt stop httpd

sudo systemclt start httpd
```
