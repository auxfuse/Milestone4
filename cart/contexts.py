from django.shortcuts import get_object_or_404
from membership.models import Membership


def cart_contents(request):
    """Allow cart contents to maintain across app session"""

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for id in cart.items():
        membership = get_object_or_404(Membership, pk=id)
        total += membership.price
        cart_items.append(
            {
                'id': id,
                'membership': membership,
            }
        )

    return {
        'cart_items': cart_items,
        'total': total
    }
