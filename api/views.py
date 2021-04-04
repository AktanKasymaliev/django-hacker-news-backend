from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment, UpvotePost, ReplyComment
from .serializers import PostListSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    