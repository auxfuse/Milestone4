from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import MakePaymentForm, OrderForm
from membership.models import Membership
from .models import OrderLineItem
import stripe

stripe.api_key = settings.STRIPE_SECRET


# Create your views here.
def checkout(request):
    """Ensure user is logged in, if so, check if both order & payment forms
    are valid with required information. Save each to respective tables in DB
    and charge customer, if paid successful, clear cart and redirect to
    membership with success message, otherwise throw error message with
    redirect to membership page. If user not logged throw error detailing
    same and redirect to membership page."""
    if request.user.is_authenticated:
        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.user = request.user
                order.save()

                cart = request.session.get('cart', {})
                total = 0
                for id, quantity in cart.items():
                    membership = get_object_or_404(Membership, pk=id)
                    total += quantity * membership.price
                    order_line_item = OrderLineItem(
                        order=order,
                        membership=membership,
                        quantity=quantity
                    )
                    order_line_item.save()

                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    messages.success(request, 'Payment received, Thank you!')
                    request.session['cart'] = {}
                    return redirect('membership')

                messages.error(request,
                               'We were unable to take payment with that card.')

            print(payment_form.errors)
            messages.error(request,
                           'We were unable to take payment with that card.')
            return redirect('membership')

        context = {
            'payment_form': MakePaymentForm,
            'order_form': OrderForm,
            'publishable': settings.STRIPE_PUBLISHABLE
        }

        return render(request, 'checkout/checkout.html', context)

    messages.error(request, 'Please login before attempting to access Cart.')
    return redirect('membership')
