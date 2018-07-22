# jobs
Platform to post and search for jobs

### User Features
- Browse Jobs List By Category
- Search for Jobs by using Text
- Filter jobs by Category
- Subscribe mailing list for new jobs filtered by category

### Company Features
- Post Jobs


## Development Environment

### In order to run this project you will need:

- Python virtual environment with minimum 3.6 version installed
- Pipenv
- Django 2.0+

#### How to install

```
$ pip install pipenv

$ git clone https://github.com/mauricioabreu/jobs.git

$ cd jobs

$ pipenv --python 3.6

$ pipenv shell

$ pipenv install --dev
```

Setup the initial database
```
$ cd workremotely

$ python manage.py migrate
```


#### How to test

```
$ cd workremotely

$ python manage.py test
```

#### How to run
```
$ cd workremotey

$ python manage.py runserver
```
