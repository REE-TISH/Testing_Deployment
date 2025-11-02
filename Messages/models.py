from django.db import models
from ComicData.models import ComicGroup,Chapter

# Create your models here.
class ComicGroupMessage(models.Model):
    comic_group = models.ForeignKey(ComicGroup, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.sender} in {self.comic_group.name}: {self.body[:30]}..."


class Comments(models.Model):
    sender = models.CharField(max_length=150,blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=200,blank=True,null=True)
    related_chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE,related_name='ChapterComments')
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender} sent {self.body}'

class InboxComments(models.Model):
    sender = models.CharField(max_length=150,blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=200,blank=True,null=True)
    ParentMsg = models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='CommentsChild')

    def __str__(self):
        return f'{self.sender} sent {self.body}'
    
