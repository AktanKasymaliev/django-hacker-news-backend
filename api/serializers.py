from rest_framework import serializers, response, status
from .models import Post, UpvotePost, Comment, ReplyComment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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
        representation['author_name'] = instance.author_name.username
        representation['upvotes'] = self.get_vote_count(instance)
        representation['comments'
        ] = instance.comment_post.count() + instance.reply_comment.count()
        representation['replied_comments'] = instance.reply_comment.count()
        return representation


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ('id', 'title', 'link')

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.title = validated_data.get('title', instance.title)
        instance.link = validated_data.get('link', instance.link)
        instance.author_name = request.user
        instance.save()
        return instance

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link')

    def create(self, validated_data):
        request = self.context.get('request')
        post = Post.objects.create(
            author_name=request.user,
            **validated_data
        )
        return post

class PostDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
     

# Working with upvote object
class UpvoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotePost
        fields = ('id', 'author', 'post', 'upvote')

    def to_representation(self, instance):
        representation = super(UpvoteListSerializer, self).to_representation(instance)
        representation['author'] = instance.author.username
        representation['post'] = instance.post.title
        return representation

class UpvoteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotePost
        fields = ('id', 'post', 'upvote')
        
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

class UpvoteDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotePost

# Working with comment object
# List comment
class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author_name', 'content', 'creation_date')

    def to_representation(self, instance):
        representation = super(CommentsListSerializer, self).to_representation(instance)
        representation['replied_comments'] = instance.comment.count()
        representation['author_name'] = instance.author_name.username
        representation['post'] = instance.post.title
        return representation

# Create 
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'content')

    def create(self, validated_data):
        request = self.context.get('request')
        comment = Comment.objects.create(
            author_name=request.user,
            **validated_data)
        return comment

    def to_representation(self, instance):
        representation = super(CommentCreateSerializer, self).to_representation(instance)
        representation['author_name'] = instance.author_name.username
        representation['post'] = instance.post.title
        return representation

# RUD comment 
class CommentRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post', 'author_name', 'content', 'creation_date')

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.post = validated_data.get('post', instance.post)
        instance.author_name = request.user
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super(CommentRUDSerializer, self).to_representation(instance)
        representation['post'] = instance.post.title
        representation['author_name'] = instance.author_name.username
        representation['replied_comments'] = ReplyCommentSerializer(
        instance.comment.all(), many=True
        ).data
        return representation


# work with ReplyComment
class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id', 'post', 'author', 'comment', 'message', 'sent_at')

    def to_representation(self, instance):
        representation = super(ReplyCommentSerializer, self).to_representation(instance)
        representation['post'] = instance.post.title
        representation['author'] = instance.author.username
        return representation


class ReplyCreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id', 'post', 'comment', 'message')

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


#Register User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        if validated_data:
            user = User.objects.create(username=validated_data.get('username'),
                                        email=validated_data.get('email'))
            user.set_password(validated_data.get('password')) 
            user.save()
            return user
        else:
            raise serializer.ValidationError('Sorry, but your inputed data is not correctly')

    def validation_password(self, value):
        return make_password(value)
