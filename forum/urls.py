from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum-posts'),
    path('filtered-posts', views.filter_posts, name='filtered-posts'),
    path('create-post', views.create_post, name='create-post'),
    path('view-post/<int:post_id>', views.view_post, name='view-post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit-post'),
    path('edit-post/<int:post_id>/delete/', views.del_post, name='del-post')
]
