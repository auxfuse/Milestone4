from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.models import auth
from .forms import UserRegistrationForm, UserLogin
from forum.models import Post


# Create your views here.
def register(request):
    """Register User if username & email fields are unique and not already
    taken, also check if password fields match. If all checks are made return
    user to Index page with success message of registration and instant
    login. If user is already logged in, display error message."""
    if request.method == 'POST':
        # Get form values
        reg_form = UserRegistrationForm(request.POST)

        # Ensure form validations are met
        if reg_form.is_valid():
            user = reg_form.save()
            auth.login(request, user)
            messages.success(request, 'You are now registered & logged in.')
            return redirect('index')

    elif request.user.is_authenticated:
        messages.error(request, 'You are logged in already!')
        return redirect(request, 'index')
    else:
        reg_form = UserRegistrationForm()

    context = {
        'register_page': 'active',
        'form': reg_form
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """Log user in and redirect to Index page with success message.
    Display error messaging if already logged in, or if wrong credentials
    used to log in with."""
    if request.user.is_authenticated:
        messages.error(request, 'You are logged in already!')
        return redirect('index')
    elif request.method == 'POST':
        login_form = UserLogin(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                auth.login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid Login details!')
                return redirect('login')
    else:
        login_form = UserLogin()

    context = {
        'login-page': 'active',
        'form': login_form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    """Logout User, redirect to Home page & display success message."""
    logout(request)
    messages.success(request, "Thank you! You have successfully logged out.")
    return redirect('index')


def dashboard(request):
    """Function to direct User to bespoke dashboard containing details
    about Posts they own as well as commented on, & display any membership
    options they may have purchased. """
    forum_posts = Post.objects.order_by('-date_posted')
    user = request.user
    print(user)
    my_posts = forum_posts.filter(originator__exact=user)

    # Paginator
    paginator = Paginator(my_posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'dashboard_page': 'active',
        'posts': paged_posts
    }

    return render(request, 'accounts/dashboard.html', context)
