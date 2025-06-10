from django.http import HttpResponse
from django.db import connection


def vulnerable(request):
    """A deliberately vulnerable view vulnerable to SQL injection."""
    name = request.GET.get("name", "")
    with connection.cursor() as cursor:
        # WARNING: This is intentionally vulnerable and should not be used in production.
        cursor.execute(
            "SELECT id, name FROM insecure_app_item WHERE name = '%s'" % name
        )
        rows = cursor.fetchall()
    return HttpResponse(
        ", ".join(str(row[1]) for row in rows) or "No matching items"
    )

