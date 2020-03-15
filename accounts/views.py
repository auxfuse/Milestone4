from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    context = {
        'register_page': 'active'
    }

    return render(request, 'accounts/register.html', context)


def login(request):
    context = {
        'login_page': 'active'
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    return redirect('index')


def dashboard(request):
    context = {
        'dashboard_page': 'active'
    }

    return render(request, 'accounts/dashboard.html', context)
