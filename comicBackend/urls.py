from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ComicData.urls')),  # Include URLs from ComicData app
    path('messages/', include('Messages.urls')),  # Include URLs from Messages app
]

