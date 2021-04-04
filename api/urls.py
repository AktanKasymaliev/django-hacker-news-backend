from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # posts 
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),

    # upvotes 
    path('upvotes/', UpvoteListView.as_view(), name='upvotes'),
    path('upvote/add/', UpvoteAddView.as_view(), name='upvote_add'),

    # comments 
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/', CommentRUDView.as_view(), name='comment'),

    # replycomments
    path('replies/comments/', ReplyCommentView().as_view(), name='reply_comment'),
    path('reply/', ReplyCreateComment.as_view(), name='reply_comment_create'),
    path('reply/delete/<int:pk>/', ReplyDeleteCommentView.as_view(), name='reply_comment_delete'),
]