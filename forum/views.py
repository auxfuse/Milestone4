from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Post


# Create your views here.
def forum(request):

    forum_posts = Post.objects.order_by('-date_posted')

    # Paginator
    paginator = Paginator(forum_posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    """Render Forum page and return all available posts with pagination and
    search functionality."""
    context = {
        'forum_page': 'active',
        'posts': paged_posts
    }

    return render(request, 'forum/forum.html', context)


def forum_post(request):
    """Create Forum Post."""
    return render(request, 'forum/post.html')
