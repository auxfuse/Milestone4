from django.shortcuts import render, redirect, get_object_or_404
from .models import Membership


# Function Views
def membership(request):
    memberships = Membership.objects.all().order_by('price')

    context = {
        'membership_page': 'active',
        'memberships': memberships
    }

    return render(request, 'membership/membership.html', context)
