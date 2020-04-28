from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactQuery


# Function Views
def contact(request):
    """Render contact template and ContactQuery form. Once form is filled
    out, save and display to the Admin dashboard with email to admin."""
    if request.method == 'POST':
        contact_form = ContactQuery(request.POST)

        if contact_form.is_valid():
            messages.success(request, 'Mail sent. We will be in touch.')
            return redirect('index')

    context = {
        'form': ContactQuery
    }

    return render(request, 'contact/contact.html', context)
