.PHONY: test

bootstrap:
	pip install -r requirements.txt
	createdb -U postgres access_mo_django
	python am/manage.py migrate
	python am/manage.py collectstatic --noinput
	python am/manage.py runserver

test:
	coverage run am/manage.py test general
	coverage run am/manage.py test legislative
	coverage run am/manage.py test finance
	coverage run am/manage.py test search
	coverage report -m