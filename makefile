install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	echo 'db_name=' >> .env
	echo 'db_host=' >> .env
	echo 'db_port=' >> .env
	echo 'db_user=' >> .env
	echo 'db_pass=' >> .env
	echo 'django_secret=' >> .env
	
migrate:
	python3 manage.py makemigrations &&\
		python3 manage.py migrate

run:
	python3 manage.py runserver