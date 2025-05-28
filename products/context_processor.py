# myapp/context_processors.py
from accounts.models import Cart, CartItem

def cart_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_paid=False).first()
        if cart:
            return {'cart_item_count': CartItem.objects.filter(cart=cart).count()}
    return {'cart_item_count': 0}