from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Novels

class TestNovels(TestCase):
    def setUp(self):
        self.novel = Novels.objects.create(
            title="Comic One", author="Author A", description="Description of Comic One",published_date="2023-01-01",content='hello'
        )

        self.client = APIClient()

    