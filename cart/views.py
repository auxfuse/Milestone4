from django.shortcuts import render, reverse, redirect
from django.contrib import messages


# Function Views
def view_cart(request):
    """Render Cart template & cart contents if any membership has been
    selected by user"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, membership_id):
    """Add membership plan to cart"""
    cart = request.session.get('cart', {})

    cart[membership_id] = cart.get(membership_id)

    request.session['cart'] = cart
    messages.success(request, 'Membership Plan added to Cart!')
    return redirect('membership')


def del_from_cart(request):
    """Remove membership plan from cart, or in our case, as only one
    membership can be added to cart at any given time aka `clear cart`"""
    cart = request.session.get('cart', {})

    cart.clear()
    request.session['cart'] = cart
    messages.success(request, 'Cart has been emptied.')
    return redirect('membership')
