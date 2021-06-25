[![pipeline status](https://git.socservice.kg/azamattokhtaev/mz-license/badges/master/pipeline.svg)](https://git.socservice.kg/azamattokhtaev/mz-license/-/commits/master)
[![coverage report](https://git.socservice.kg/azamattokhtaev/mz-license/badges/master/coverage.svg)](https://git.socservice.kg/azamattokhtaev/mz-license/-/commits/master)


# Aircraft monitoring system(TEST)

The service uses the following technologies:

- `Python 3.8`
- `Django 3.2`
- `Gunicorn`
- `PostgreSQL 12.4`
- `Docker`

## How to run development environment
##### Download and install postgres version 12.4
link to download - https://www.postgresql.org/download/

```sh
$ sudo -u postgres createdb aircraft # creating a database with name shashka.
```

```sh
$ git clone git@github.com:Sultanbek9899/aircraft_monitoring.git && cd mz-license
$ cp .env.example .env # or see environment variables below.
$ export $(cat .env | xargs) # to activate environment variables
$ mkvirtualenv mz-license
$ pip install -r requirements/development.txt
$ python manage.py migrate # add migration into database.
$ python manage.py runserver # run backend.
```

## How to run production environment via docker
Production environment start via Gitlab CI service.   
Use `git clone git@github.com:Sultanbek9899/aircraft_monitoring.git`   
Use `docker-compose up --build -d` for pull images and start


### Environment variables

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SETTINGS_MODULE`  | Django secret key  | django-insecure-s&62-4&i29ofvx3gzg4-=*lohg+wk3axhyona2*s79f#cku+tj             |
| `DJANGO_ALLOWED_HOSTS`  | A list of strings representing the host/domain names that this backend can serve  | localhost,127.0.0.1,0.0.0.0              |
| `DATABASE_URL`  | Database url for connection with a backend | export DATABASE_URL=db://aircraft_user:aircraft2021@127.0.01:5432/aircraft2021 |
| `POSTGRES_USER`  | Postgres username |   aircraft_user   |
| `POSTGRES_PASSWORD`  | Postgres password | aircraft2021    |
| `POSTGRES_DB`  | Postgres database name | aircraft |
| `POSTGRES_HOST`  | Postgres host | 127.0.0.1 |
| `SENTRY_DSN`  | Sentry DSN | None |
