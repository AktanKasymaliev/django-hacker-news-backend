from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # jwt auth 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # user 
    path('registration/', RegisterUserView.as_view(), name='register'),

    # posts 
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),

    # upvotes 
    path('upvotes/', UpvoteListView.as_view(), name='upvotes'),
    path('upvote/add/', UpvoteAddView.as_view(), name='upvote_add'),
    path('upvote/remove/<int:pk>/', UpvoteDeleteView.as_view(), name='upvote_remove'),

    # comments 
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/', CommentRUDView.as_view(), name='comment'),

    # replycomments
    path('replies/comments/', ReplyCommentView().as_view(), name='reply_comment'),
    path('reply/', ReplyCreateComment.as_view(), name='reply_comment_create'),
    path('reply/delete/<int:pk>/', ReplyDeleteCommentView.as_view(), name='reply_comment_delete'),
]