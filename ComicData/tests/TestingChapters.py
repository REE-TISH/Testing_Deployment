from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Chapter,Comic

class TestChapter(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.comic1 = Comic.objects.create(title="Comic One", author="Author A", description="Description of Comic One",published_date="2023-01-01")
        self.chapter1 = Chapter.objects.create(comic=self.comic1,title='Chapter1',chapter_number=1)
        self.chapter2 = Chapter.objects.create(comic=self.comic1,title='Chapter 2',chapter_number=2)

    def test_GetsChapterOfGivenNumber(self):
        response = self.client.get(reverse('chapter',kwargs={'comic_id':1,'id':2}))
        
        self.assertEqual(response.data['id'],self.chapter2.id)