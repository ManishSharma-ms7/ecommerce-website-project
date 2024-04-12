from .models import Cart, CartItem
from .views import _cart_id
from django.db.models import Sum

def counter(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart_count = 0
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            # cart_items = CartItem.objects.all().filter(cart_id=cart).aggregate(Sum('quantity'))
            cart_items = CartItem.objects.all().filter(cart_id=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
