from django.urls import path
from . import views

urlpatterns = [
    path('group/<str:group_id>', views.ComicGroupMessageListView.as_view(), name='comic-group-message-list'),
    path('commentList/<str:comic_id>/<str:chapter_no>/',views.CommentListView.as_view(),name='comment-list'),
    path('addComments/<str:comic_id>/<str:chapter_no>/',views.CommentAddFunction,name='comment-add'),
    path('addInBoxComment/<str:comment_id>/',views.InBoxCommentAddView,name='Inbox-comment'),
]
