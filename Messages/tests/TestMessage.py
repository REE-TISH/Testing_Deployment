from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import ComicGroupMessage
from ComicData.models import ComicGroup

class TestMessageForNoMessageInGroup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.comic_group = ComicGroup.objects.create(name="Test Comic Group")

    def test_no_messages_in_comic_group(self):
        response = self.client.get(reverse('comic-group-message-list', kwargs={'group_id': self.comic_group.id}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"detail": "No messages found for this comic group."}, "Expected no messages message when the group has no messages.")


        