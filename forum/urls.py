from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum, name='forum-posts')
]
