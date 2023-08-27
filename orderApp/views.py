from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order
from shopApp.models import Product


# Create your views here.


@login_required
def addToCard(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchase=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItem.filter(item=item).exists():
            order_item[0].quantity +=1
            order_item[0].save()
            messages.success(request, 'Item Quintity Is update!')
            return redirect('homeApp:home')
        else:
            order.orderItem.add(order_item[0])
            messages.success(request, 'Item added to your card!')
            return redirect('homeApp:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderItem.add(order_item[0])
        messages.success(request, 'Item added to your card!')
        return redirect('homeApp:home')
@login_required
def cardView(request):
    carts = Cart.objects.filter(user=request.user, purchase=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        context={
            "carts":carts,
            'order':order
        }
        return render(request, 'orderApp/cart.html', context)
    else:
        messages.success(request, 'You do not have any item in your cart!')
        return redirect('homeApp:home')
    

@login_required
def removeCardItem(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItem.filter(item=item, user=request.user, purchase=False):
            order_item = Cart.objects.filter(item=item, user=request.user,purchase=False)[0]
            order.orderItem.remove(order_item)
            order_item.delete()
            messages.success(request, 'Item successfully remove from your card!')
            return redirect('orderApp:card_view')
        else:
            messages.success(request, 'This item is not n your card!')
            return redirect('orderApp:card_view')
    else:
        messages.success(request, 'You do not have any active order!')
        return redirect('orderApp:card_view')
    
@login_required
def IncreaseQuintity(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItem.filter(item=item, user=request.user, purchase=False).exists():
            order_item = Cart.objects.filter(item=item, user=request.user,purchase=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity +=1
                order_item.save()
                messages.success(request, 'Item Quintity Updated!')
                return redirect('orderApp:card_view')
        else:
            messages.success(request, 'Product not found!')
            return redirect('homeApp:home')
    else:
        messages.success(request, 'Product not found!')
        return redirect('homeApp:home')
    

@login_required
def DecreaseQuanity(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderItem.filter(item=item, user=request.user, purchase=False).exists():
            order_item = Cart.objects.filter(item=item, user=request.user,purchase=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
                messages.success(request, 'Item Quintity Updated!')
                return redirect('orderApp:card_view')
        else:
            messages.success(request, 'Product not found!')
            return redirect('homeApp:home')
    else:
        messages.success(request, 'Product not found!')
        return redirect('homeApp:home')