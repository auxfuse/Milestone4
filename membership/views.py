from django.shortcuts import render


# Function Views
def membership(request):
    return render(request, 'membership/membership.html')
