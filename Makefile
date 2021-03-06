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
	coverage run am/manage.py test geo
	coverage run am/manage.py test scraper
	coverage report -m
	coverage xml

activatedb_local:
	rm -f am/am/settings_local.py
	cp am/am/settings_local.py.local am/am/settings_local.py

activatedb_stage:
	rm -f am/am/settings_local.py
	cp am/am/settings_local.py.stage am/am/settings_local.py

activatedb_prod:
	rm -f am/am/settings_local.py
	cp am/am/settings_local.py.prod am/am/settings_local.py