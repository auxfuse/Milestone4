from django.shortcuts import render, reverse, redirect
from django.contrib import messages


# Function Views
def view_cart(request):
    """Render Cart template & cart contents if any membership has been
    selected by user"""
    context = {
        'cart_page': 'active'
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, id):
    """Add membership plan to cart. If user is not logged in, redirect to
    membership template with error message detailing same. If user is logged
    in and has already added a plan to cart, and attempts to add another,
    show error message and redirect to membership template."""
    plan_qty = 1
    cart = request.session.get('cart', {})

    if request.user.is_authenticated:
        if cart.items():
            messages.error(request, 'You already have added a Plan to your cart.')
            return redirect('membership')

        cart[id] = cart.get(id, plan_qty)

        request.session['cart'] = cart
        messages.success(request, 'Membership Plan added to Cart!')
        return redirect(reverse('membership'))

    messages.error(request, 'You must be logged in to add a Plan to cart.')
    return redirect('membership')


def clear_cart(request):
    """Remove membership plan from cart, or in our case, as only one
    membership can be added to cart at any given time aka `clear cart`"""
    cart = request.session.get('cart', {})

    cart.clear()
    request.session['cart'] = cart
    messages.success(request, 'Cart has been emptied.')
    return redirect('membership')
