from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactQuery


# Function Views
def contact(request):
    """Render contact template and ContactQuery form. Once form is filled
    out, save and display to the Admin dashboard with email to admin. If
    user is a registered & logged user we capture their username for the
    admin, otherwise user is public and query_from is left blank. """
    if request.method == 'POST':
        if request.user.is_authenticated:
            create_contact_form = Contact(
                query_title=request.POST.get('query_title'),
                query_text=request.POST.get('query_text'),
                query_email=request.POST.get('query_email'),
                query_from=request.user
            )
            create_contact_form.save()
        else:
            create_contact_form = Contact(
                query_title=request.POST.get('query_title'),
                query_text=request.POST.get('query_text'),
                query_email=request.POST.get('query_email')
            )
            create_contact_form.save()

        messages.success(request, 'Mail sent. We will be in touch.')
        return redirect('index')

    context = {
        'form': ContactQuery
    }

    return render(request, 'contact/contact.html', context)
