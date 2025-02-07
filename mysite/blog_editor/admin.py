from django.contrib import admin
from .models import Comment, Blog, Post, Author

admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Author)
