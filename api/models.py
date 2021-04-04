from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UpvotePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='upvote')
    upvote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Vote for {self.post}"


class Comment(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name}"


class ReplyComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.comment}"

