from django.test import Client, TestCase

from .models import Item


class VulnerableViewTests(TestCase):
    def setUp(self):
        Item.objects.create(name="safe")
        Item.objects.create(name="other")
        self.client = Client()

    def test_regular_query(self):
        response = self.client.get("/vulnerable/", {"name": "safe"})
        self.assertContains(response, "safe")

    def test_sql_injection(self):
        payload = "safe' OR '1'='1"
        response = self.client.get("/vulnerable/", {"name": payload})
        self.assertIn("other", response.content.decode())

