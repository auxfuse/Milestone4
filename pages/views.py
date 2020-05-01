from django.shortcuts import render
from coaches.models import StaffMember


# Function views
def index(request):
    """Render Index page"""
    context = {
        'home_page': 'active'
    }
    return render(request, 'pages/index.html', context)


def about(request):
    """Render About page and staff_members ordered by employed_on date in
    ascending order."""
    staff_members = StaffMember.objects.order_by('employed_on')

    context = {
        'about_page': 'active',
        'staff_members': staff_members
    }
    return render(request, 'pages/about.html', context)


def accessibility(request):
    """Render basic Accessibility page."""
    return render(request, 'pages/accessibility.html')


def privacy(request):
    """Render basic Privacy page."""
    return render(request, 'pages/privacy.html')
