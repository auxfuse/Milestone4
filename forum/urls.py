from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum-posts'),
    path('create-post', views.create_post, name='create-post'),
    path('view-post/<int:post_id>', views.view_post, name='view-post'),
]
