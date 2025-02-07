from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path("blog/<int:blog_id>/", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post, name="post"),
]