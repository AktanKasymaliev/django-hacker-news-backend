from rest_framework import serializers, response
from .models import Post, UpvotePost, Comment, ReplyComment
from functools import reduce
# Work with post object
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'creation_date', 'author_name')
    
    def get_vote_count(self, instance):
        votes = [i.upvote for i in instance.post.all()]
        count = 0
        for i in votes:
            count += i
        return count

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['upvotes'] = self.get_vote_count(instance)
        return representation



class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'link', 'author_name')


class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
     

# Working with upvote object
class UpvoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotePost
        fields = ('id', 'author', 'post', 'upvote')

class UpvoteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotePost
        fields = ('post', 'upvote')
        
    def validate(self, attrs):
        request = self.context.get('request')
        if attrs['upvote'] != 1:
            raise serializers.ValidationError("you cannot set other number, except 1")
        elif UpvotePost.objects.filter(
            author=request.user
        ).exists():
            raise serializers.ValidationError("you cannot vote anymore")
        else:
            return attrs 

    def create(self, validated_data):
        request = self.context.get('request')
        vote = UpvotePost.objects.create(
            author=request.user,
            **validated_data
        )
        return vote

# Working with comment object
# List comment
class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author_name', 'content', 'creation_date')

    def to_representation(self, instance):
        representation = super(CommentsListSerializer, self).to_representation(instance)
        representation['replied_comments'] = instance.comment.count()
        return representation

# Create 
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'content')

    def create(self, validated_data):
        request = self.context.get('request')
        comment = Comment.objects.create(
            author_name=request.user,
            **validated_data)
        return comment

# RUD comment 
class CommentRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post', 'author_name', 'content', 'creation_date')

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.post = validated_data.get('post')
        instance.author_name = request.user
        instance.content = validated_data.get('content')
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super(CommentRUDSerializer, self).to_representation(instance)
        representation['replied_comments'] = ReplyCommentSerializer(
        instance.comment.all(), many=True
        ).data
        return representation


# work with ReplyComment
class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id', 'post', 'author', 'comment', 'message', 'sent_at')


class ReplyCreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('post', 'comment', 'message')

    def create(self, validated_data):
        request = self.context.get('request')
        comment = ReplyComment.objects.create(
            author=request.user,
            **validated_data
        )
        return comment

class ReplyDeleteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
