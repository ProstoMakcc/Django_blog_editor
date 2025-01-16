from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Creation Date")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment written by {self.author} on {self.post.title}"

class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Creation Date")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return f"{self.title} written by {self.author}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, blank=True)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Creation Date")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
    
