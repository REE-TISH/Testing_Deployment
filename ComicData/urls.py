from django.urls import path
from . import views

urlpatterns = [ 
    path('comics/', views.ComicListView.as_view(), name='comic-list'),
    path('comics/<int:id>/',views.ComicDetailView.as_view(),name='comic'),
    path('comic-groups/', views.ComicGroupListView.as_view(), name='comic-group-list'),
    path('comic-groups/<int:id>/', views.ComicGroupDetailView.as_view(), name='comic-group-detail'),
    path('comics/<int:comic_id>/chapter/<int:id>/',views.ChapterView.as_view(),name='chapter'),
    path('novels/',views.NovelListView.as_view(),name='novel-list'),
    path('novel/<str:pk>/',views.NovelView.as_view(),name='novel-view'),
    path('novel/<str:novel_id>/chapter/<str:id>/',views.NovelChapterView.as_view(),name='chapter-view')

]