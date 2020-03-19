from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    context = {
        'register_page': 'active'
    }

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check Password match
        if password == password2:
            # Check if username is unique
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already used.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already coupled to an '
                                        'account.')
                return redirect('register')
            else:
                # Register User in Users collection & redirect to Home page.
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                auth.login(request, user)
                messages.success(request, 'You are now registered & logged in.')
                return redirect('index')
        else:
            messages.error(request, 'Passwords did not match, try again.')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)


def login(request):
    context = {
        'login_page': 'active'
    }

    # Get login form values.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password
        )

        # Check if user exists & login if yes otherwise show error.
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Login details.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', context)


def logout(request):
    return redirect('index')


def dashboard(request):
    context = {
        'dashboard_page': 'active'
    }

    return render(request, 'accounts/dashboard.html', context)
