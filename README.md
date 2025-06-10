# Django SQL Injection Demo

This minimal Django project demonstrates an intentional SQL injection vulnerability for testing code analysis tools. It contains one model (`Item`) and a view that performs a raw SQL query using untrusted input.

## Running

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit `/vulnerable/?name=VALUE` to query the database. Supplying SQL content such as `safe' OR '1'='1` will demonstrate the vulnerability.
