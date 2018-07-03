am-django-project
=================

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0d1172745ea9433a8eec5982e8d8b058)](https://app.codacy.com/app/NathanLawrence/am-django-project?utm_source=github.com&utm_medium=referral&utm_content=access-missouri/am-django-project&utm_campaign=badger)
[![Documentation Status](https://readthedocs.org/projects/access-missouri/badge/?version=latest)](https://access-missouri.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/access-missouri/am-django-project.svg?branch=master)](https://travis-ci.org/access-missouri/am-django-project)
[![Coverage Status](https://coveralls.io/repos/github/access-missouri/am-django-project/badge.svg?branch=master)](https://coveralls.io/github/access-missouri/am-django-project?branch=master)

Integration hub for all Access Missouri data sets (built in Django).

## Usage and Full Documentation
This is a pretty big project with tens of thousands of lines of code and tons of different data sources. To keep things organized and simplify the process of learning what you need to know, most major documentation now happens in [the project wiki](https://github.com/access-missouri/am-django-project/wiki).

## In Brief

Requires:

* Python 2.7 (currently testing 3.5 also)
* PostgreSQL 9.4 or greater

To bootstrap the project locally:
```bash
make bootstrap
```

To run tests locally:
```bash
make test
```

