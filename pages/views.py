from django.shortcuts import render
from coaches.models import StaffMember


# Create your views here.
def index(request):
    context = {
        'home_page': 'active'
    }

    return render(request, 'pages/index.html', context)


def about(request):
    staff_members = StaffMember.objects.order_by('employed_on')

    context = {
        'about_page': 'active',
        'staff_members': staff_members
    }

    return render(request, 'pages/about.html', context)


def accessibility(request):
    return render(request, 'pages/accessibility.html')


def privacy(request):
    return render(request, 'pages/privacy.html')
