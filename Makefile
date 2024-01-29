manage_py := python ./currency/manage.py

run:
	$(manage_py) runserver 0.0.0.0:8000

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake:
	flake8 currency/

worker:
	cd currency && celery -A settings worker -l info --autoscale 1,10

beat:
	cd currency && celery -A settings beat -l info