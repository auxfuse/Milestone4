from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html')


def forum_post(request):
    return render(request, 'forum/post.html')
