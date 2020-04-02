from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def forum(request):
    """Render Forum page and return all available posts with pagination and
    search functionality."""
    context = {
        'forum_page': 'active',
        'posts': Post.objects.all()
    }

    return render(request, 'forum/forum.html', context)


def forum_post(request):
    """Create Forum Post."""
    return render(request, 'forum/post.html')
