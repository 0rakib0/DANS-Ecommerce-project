from django import template
from orderApp.models import Order, Cart
from shopApp.models import WishList


register = template.Library()


@register.filter
def cart_total(user):
    order = Cart.objects.filter(user=user, purchase=False)


    if order.exists():
        return order.count()
    else:
        return 0
@register.filter
def wishListTotal(user):
    wishlist = WishList.objects.filter(user=user)
    if wishlist.exists():
        return wishlist.count()
    else:
        return 0