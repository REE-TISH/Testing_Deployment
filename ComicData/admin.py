from django.contrib import admin
from .models import Comic, Chapter,ComicGroup,NovelChapter,Novels

admin.site.register(Comic)
admin.site.register(Chapter)
admin.site.register(ComicGroup)
admin.site.register(NovelChapter)
admin.site.register(Novels)
# Register your models here.
