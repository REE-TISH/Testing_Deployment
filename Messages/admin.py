from django.contrib import admin
from .models import ComicGroupMessage,Comments,InboxComments
# Register your models here.

admin.site.register(ComicGroupMessage)
admin.site.register(Comments)
admin.site.register(InboxComments)
