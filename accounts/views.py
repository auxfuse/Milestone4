from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def register(request):
    context = {
        'register_page': 'active'
    }

    if request.method == 'POST':
        messages.error(request, 'User already exists')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)


def login(request):
    context = {
        'login_page': 'active'
    }

    if request.method == 'POST':
        messages.error(request, 'Load of no....')
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
