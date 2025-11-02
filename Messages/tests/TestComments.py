from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import ComicGroupMessage,Comments
from ComicData.models import Comic,Chapter



class TestAddCommentsView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.commic = Comic.objects.create(
            title='testRun',
            author='Reetsih',
            description='Please work',
            published_date='2025-12-03',
            rating=4.9
            
        )
        self.chapter = Chapter.objects.create(
            comic=self.commic,
            title='heljfsad',
            chapter_number = 1
        )
    
    def test_postRequest_api(self):
        data = {
            'sender':'Reetish',
            'body':'how are you',
            'user_id':'fdaklfjasf'
        }
        response = self.client.post(reverse('comment-add',kwargs={'comic_id':1,'chapter_no':1}),data)

        self.assertEqual(response.status_code,200)




