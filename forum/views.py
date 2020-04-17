from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Post, PostComment
from .forms import CreatePost, CreateComment, FilterForm


# Function Views
def forum(request):
    """Render Forum page and return all available posts with pagination and
    search functionality."""
    forum_posts = Post.objects.order_by('-date_posted')

    # Paginator
    paginator = Paginator(forum_posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'forum_page': 'active',
        'form': FilterForm,
        'posts': paged_posts
    }

    return render(request, 'forum/forum.html', context)


def filter_posts(request):
    """Display categorised results based on Filter selection by User on
    Forum page"""
    queryset = Post.objects.order_by('-date_posted')

    if 'category_filter' in request.GET:
        category_filter = request.GET['category_filter']
        if category_filter:
            queryset = queryset.filter(category__iexact=category_filter)

    context = {
        'posts': queryset
    }

    return render(request, 'forum/filtered-posts.html', context)


def view_post(request, post_id):
    """View Forum Post and render Comment Form & add comments to thread."""
    post = get_object_or_404(Post, pk=post_id)
    post_comments = PostComment.objects.filter(post_id=post_id).order_by(
        '-date_commented')

    if request.method == 'POST':
        create_comment_form = PostComment(
            comment_text=request.POST.get('comment_text'),
            commenter=request.user,
            post=post
        )
        create_comment_form.save()
        messages.success(request, 'Comment added to Post')
        return redirect('view-post', post_id)

    context = {
        'post': post,
        'comments': post_comments,
        'form': CreateComment
    }

    return render(request, 'forum/view-post.html', context)


def create_post(request):
    """Render Create Post and Create Post for display to the Forum"""
    if request.method == 'POST':
        # Get form values
        create_post_form = Post(
            title=request.POST.get('title'),
            post_text=request.POST.get('post_text'),
            category=request.POST.get('category'),
            originator=request.user
        )

        create_post_form.save()
        messages.success(request, 'Post added to the Forum!')
        return redirect('forum-posts')

    context = {
        'form': CreatePost
    }

    return render(request, 'forum/create-post.html', context)
