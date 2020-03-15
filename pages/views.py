from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'home_page': 'active'
    }

    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'about_page': 'active'
    }

    return render(request, 'pages/about.html', context)


def accessibility(request):
    return render(request, 'pages/accessibility.html')


def privacy(request):
    return render(request, 'pages/privacy.html')
