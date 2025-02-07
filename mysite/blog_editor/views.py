from django.shortcuts import render, get_object_or_404
from .models import Post, Blog

def post_list(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    posts = Post.objects.filter(blog=blog)

    return render(request, 'blog_editor/post_list.html', {"posts": posts,
                                                          "blog": blog})

def blog_list(request):
    blogs = Blog.objects.all()

    return render(request, 'blog_editor/blog_list.html', {"blogs": blogs})

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    blog_id = post.blog.id

    return render(request, 'blog_editor/post.html', {"post": post,
                                                     "blog_id": blog_id})