from rest_framework import serializers
from .models import Post, UpvotePost, Comment, ReplyComment

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
        