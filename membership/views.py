from django.shortcuts import render
from .models import Membership


# Function Views
def membership(request):
    """Render all available memberships and order in ascending order on price"""
    memberships = Membership.objects.all().order_by('price')

    context = {
        'membership_page': 'active',
        'memberships': memberships
    }
    return render(request, 'membership/membership.html', context)
