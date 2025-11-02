from django.db import models

#Comic model to store comic details
class Comic(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover_image = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.JSONField(blank=True, null=True)  # Store genres as a list of strings
    

    def __str__(self):
        return self.title

#Chapter model to store chapter details related to a comic
class Chapter(models.Model):
    comic = models.ForeignKey(Comic, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    chapter_number = models.IntegerField()
    Chapter_image = models.JSONField(blank=True, null=True)  # Store chapter images as a list of URLs

    def __str__(self):
        return f"{self.comic.title} - Chapter {self.chapter_number}: {self.title}"

    class Meta:
        ordering = ['chapter_number']

# Chat Group where user who are interested in the same comic can join
class ComicGroup(models.Model):
    name = models.CharField(max_length=150)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Novels(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover_image = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class NovelChapter(models.Model):
    novel = models.ForeignKey(Novels,on_delete=models.CASCADE,related_name='novelChapters')
    title = models.CharField(max_length=200)
    chapter_no = models.IntegerField()
    Content = models.TextField()

    def __str__(self):
        return f'{self.novel.title}s chapter no {self.chapter_no}'
    
    class Meta:
        ordering = ['chapter_no']