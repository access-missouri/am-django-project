.PHONY: test

bootstrap:
	pip install -r requirements.txt
	createdb -U postgres access_mo_django
	python am/manage.py migrate
	python am/manage.py collectstatic --noinput
	python am/manage.py runserver

test:
	coverage run am/manage.py test senate_scraper
	coverage run am/manage.py test house_scraper
	coverage report -m