## Initial setup
* `git clone https://github.com/ahsanhabib91/trydjango_2_0.git`
* `cd trydjango_2_0`
* `virtualenv -p python3 .`
* `source bin/activate` (if in a terminal)
* `pip install -r requirements.txt`
* `cd src`

## Postgresql setup
* `psql -U postgres`
* `CREATE DATABASE trydjango_2_0;`

## After DB setup
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser`(Optional)
* `python manage.py runserver`

### If want to export packagelist
* `Navigate to trydjango_2_0`
* `pip freeze > requirements.txt`
