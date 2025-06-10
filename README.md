# Django SQL Injection Demo

This minimal Django project demonstrates an intentional SQL injection vulnerability for testing code analysis tools. It contains one model (`Item`) and a view that performs a raw SQL query using untrusted input.

## Prerequisites

* [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Running

```bash
uv sync
uv run manage.py migrate
uv run manage.py runserver
```

Visit `/vulnerable/?name=VALUE` to query the database. Supplying SQL content such as `safe' OR '1'='1` will demonstrate the vulnerability.

## Scanning with Sonar

```
export SONAR_TOKEN=
export SONAR_HOST_URL=
uv run pysonar
```
