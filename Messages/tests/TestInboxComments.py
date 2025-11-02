from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import ComicGroupMessage,Comments
from ComicData.models import Comic,Chapter


class TestInBoxComments(TestCase):
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
        self.comment = Comments.objects.create(
            sender='Reetish',
            body='how are you',
            user_id='jfkladsfasdf',
            related_chapter = self.chapter
            )
        
    def test_InBoxCommentPOST(self):
        data = {
            'sender':'Reetish',
            'body':'how are you',
            'user_id':'fdaklfjasf'
        }
        
        response = self.client.post(reverse('Inbox-comment',kwargs={'comment_id':self.chapter.id}),data)
        print(response.json())
        self.assertEqual(response.status_code,200)