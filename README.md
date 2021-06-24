[![pipeline status](https://git.socservice.kg/azamattokhtaev/mz-license/badges/master/pipeline.svg)](https://git.socservice.kg/azamattokhtaev/mz-license/-/commits/master)
[![coverage report](https://git.socservice.kg/azamattokhtaev/mz-license/badges/master/coverage.svg)](https://git.socservice.kg/azamattokhtaev/mz-license/-/commits/master)


# Aircraft monitoring system(TEST)

The service uses the following technologies:

- `Python 3.8`
- `Django 3.0`
- `Huey (task queue)`
- `Gunicorn`
- `NGINX 1.19`
- `PostgreSQL 12.4`
- `Redis 6.0.9`
- `Docker`

## How to run development environment
##### Download and install postgres version 12.4
link to download - https://www.postgresql.org/download/

```sh
$ sudo -u postgres createdb mz_license # creating a database with name shashka.
```

```sh
$ git clone https://git.socservice.kg/azamattokhtaev/mz-license && cd mz-license
$ cp .env.example .env # or see environment variables below.
$ export $(cat .env | xargs) # to activate environment variables
$ mkvirtualenv mz-license
$ pip install -r requirements/development.txt
$ python manage.py migrate # add migration into database.
$ python manage.py runserver # run backend.
```

## GOTENBERG
API service for generating files to pdf
[documentation](https://thecodingmachine.github.io/gotenberg/) 

## How to run production environment via docker
Production environment start via Gitlab CI service.

Use `docker-compose up --build -d` for pull images and start

# How to run tests

:exclamation: Use config -> `backend.config.settings.testing` for testing

```sh
$ export $(cat .env | xargs) # To activate environment variables
$ pytest -n 2 --cov=. --cov-report html # Run all tests
$ pytest -n 2 backend/apps/common/tests/test_index_page_view.py --cov-report html --cov=backend/apps/common/tests # Running a specific module
$ pytest -n 2 backend/apps/common/tests/test_index_page_view.py::IndexPageTestCase::test_index_page_render --cov=backend/apps/common/tests --cov-report html  # Running a specific test
```

---

### Environment variables

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SETTINGS_MODULE`  | Django secret key  | vj0q*s86^y+%8&nbp05_722*vv84%2r8g3m22_y$w*0&y6w)%)              |
| `DJANGO_ALLOWED_HOSTS`  | A list of strings representing the host/domain names that this backend can serve  | localhost,127.0.0.1,0.0.0.0              |
| `DATABASE_URL`  | Database url for connection with a backend | postgres://mz_license:mz_license@127.0.0.1:5432/mz_license |
| `POSTGRES_USER`  | Postgres username |   mz_license   |
| `POSTGRES_PASSWORD`  | Postgres password |  mz_license    |
| `POSTGRES_DB`  | Postgres database name | mz_license |
| `POSTGRES_HOST`  | Postgres host | 127.0.0.1 |
| `SENTRY_DSN`  | Sentry DSN | None |
| `EMAIL_HOST`  | Email host | test_host |
| `EMAIL_HOST_USER`  | Email host user | test_user |
| `EMAIL_HOST_PASSWORD`  | Email host password | test_password |
| `REDIS_URL`  | Redis url | redis://redis:6379/0 |
| `GOTENBERG_URI`  | Gotenberg API endpoint | None |

