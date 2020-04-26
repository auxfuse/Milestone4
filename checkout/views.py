from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import MakePaymentForm, OrderForm
from membership.models import Membership
from .models import OrderLineItem
import stripe


# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
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

                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="EUR",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, 'Your card was declined!')

                if customer.paid:
                    messages.success(request, 'Payment received, Thank you!')
                    request.session['cart'] = {}
                    return redirect('membership')
                messages.error(request, 'Something went wrong.')

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
