from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import ComicGroupMessage
from ComicData.models import ComicGroup

# Create your tests here.
class ComicGroupMessageTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.comic_group = ComicGroup.objects.create(name="Test Comic Group")
        self.message1 = ComicGroupMessage.objects.create(
            comic_group=self.comic_group,
            sender="User A",  
            body="This is a test message from User A.")

    def test_comic_group_message_list(self):
        response = self.client.get(reverse('comic-group-message-list', kwargs={'group_id': '1'}))
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.comic_group.id),str(response.data[0]['comic_group']))

