from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["user"]

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    text = models.TextField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Creation Date")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["creation_date"]

    def __str__(self):
        return f"Comment written by {self.author} on {self.post.title}"

class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, related_name="blogs", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now, verbose_name="Creation Date")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["creation_date"]

    def __str__(self):
        return f"{self.title} written by {self.author}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["author"]

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.creation_date >= timezone.now() - timezone.timedelta(days=7)
    
