.PHONY: test

bootstrap:
	pip install -r requirements.txt
	createdb -U postgres access_mo_django
	psql -c "CREATE EXTENSION postgis;" -U postgres -d access_mo_django
	python am/manage.py migrate
	python am/manage.py collectstatic --noinput
	python am/manage.py runserver

test:
	flake8 am
	# coverage run manage.py test senate_scraper
	# coverage run manage.py test house_scraper
	coverage report -m