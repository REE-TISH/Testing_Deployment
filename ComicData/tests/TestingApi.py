from django.test import TestCase
from rest_framework.test import APIClient
from ..models import Comic, ComicGroup
from django.urls import reverse 

class ComicDataApiTests(TestCase):
    def setUp(self):        
        self.client = APIClient()
        self.comic1 = Comic.objects.create(title="Comic One", author="Author A", description="Description of Comic One",published_date="2023-01-01")
       
    def test_comic_list(self):
        response = self.client.get(reverse('comic-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], self.comic1.title)
        

    def test_onComic_creation_creates_comic_group(self):
        comicGroupCreated = ComicGroup.objects.filter(name=f"{self.comic1.title} Chat Group").exists()
        self.assertTrue(comicGroupCreated, "Comic Group was not created after Comic creation")

    def test_comic_group_list(self):
        response = self.client.get(reverse('comic-group-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0, "Comic Group list is empty")
        self.assertEqual(response.data[0]['name'], f"{self.comic1.title} Chat Group")