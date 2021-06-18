install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
run:
	python3 manage.py runserver

all: install run