from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum-posts'),
    path('create-post', views.create_post, name='create-post'),
    path('forum-post', views.forum_post, name='forum-post'),
]
