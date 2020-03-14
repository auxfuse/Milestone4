from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def forum(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'forum/forum.html', context)


def forum_post(request):
    return render(request, 'forum/post.html')
