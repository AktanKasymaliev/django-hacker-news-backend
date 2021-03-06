from rest_framework import generics, status
from .models import Post, Comment, UpvotePost, ReplyComment
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import permissions, response
from .permissions import IsOwner

# work with post object
class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsOwner]

class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostDeleteSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          permissions.IsAdminUser,
                          IsOwner]


# Work with upvote object
class UpvoteListView(generics.ListAPIView):
    serializer_class = UpvoteListSerializer
    queryset = UpvotePost.objects.all()

class UpvoteAddView(generics.CreateAPIView):
    serializer_class = UpvoteAddSerializer
    queryset = UpvotePost

class UpvoteDeleteView(generics.DestroyAPIView):
    serializer_class = UpvoteDeleteSerializer
    queryset = UpvotePost



# work with comment obj 
class CommentListView(generics.ListAPIView):
    serializer_class = CommentsListSerializer
    queryset = Comment.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated,]


class CommentRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentRUDSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsOwner, permissions.IsAuthenticated, permissions.IsAdminUser]
    

# work with replycomments
class ReplyCommentView(generics.ListAPIView):
    serializer_class = ReplyCommentSerializer
    queryset = ReplyComment.objects.all()


class ReplyCreateComment(generics.CreateAPIView):
    serializer_class = ReplyCreateCommentSerializer
    queryset = ReplyComment
    permission_classes = [permissions.IsAuthenticated,]


class ReplyDeleteCommentView(generics.DestroyAPIView):
    serializer_class = ReplyDeleteCommentSerializer
    queryset = ReplyComment
    permission_classes = [IsOwner, permissions.IsAuthenticated, permissions.IsAdminUser]


# Create user
class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
