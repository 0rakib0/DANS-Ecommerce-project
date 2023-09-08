from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from shopApp.models import Product
from django.urls import reverse
from orderApp.models import Order, Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Billing_Address

# for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def Checkout(request):
    saved_address = Billing_Address.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        address = request.POST.get('address')
        zipe_code = request.POST.get('zipcode')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        billing_address = Billing_Address.objects.get(user=request.user)

        billing_address.address = address
        billing_address.zipeCode = zipe_code
        billing_address.city = city
        billing_address.country = country
        billing_address.phone = phone
        billing_address.save()
        messages.success(request, 'Address Updated!')
        return redirect('paymentApp:checkout')
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderItem.all()
    order_total = order_qs[0].getTotals
    address = Billing_Address.objects.get(user=request.user)
    context={
        'address':address,
        'order_items':order_items,
        'order_total':order_total,
    }
    return render(request, 'paymentApp/checkout.html', context)



@login_required
def Payment(request):
    saved_address = Billing_Address.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filed():
        messages.info(request, 'Please filup your shipping address!')
        return redirect('paymentApp:checkout')
    if not request.user.profile.is_fully_filed():
        messages.info(request, 'Please fillup your full information in profile!')
        return redirect('accounts:profile')
     
    store_id = 'rrras6377c57e6e7b1'
    API_key = 'rrras6377c57e6e7b1@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=API_key)
    status_url = request.build_absolute_uri(reverse('paymentApp:complate'))
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderItem.all()
    order_items_count = order_qs[0].orderItem.count()
    order_total = order_qs[0].getTotals()


    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_items_count, shipping_method='Kuriar', product_profile='None')

    corrent_user = request.user

    mypayment.set_customer_info(name=corrent_user.profile.full_name, email=corrent_user.email, address1=corrent_user.profile.address_1, address2=corrent_user.profile.address_1, city=corrent_user.profile.city, postcode=corrent_user.profile.zipcode, country=corrent_user.profile.country, phone=corrent_user.profile.phone)

    mypayment.set_shipping_info(shipping_to=corrent_user.profile.full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zipeCode, country=saved_address.country)

    response_data = mypayment.init_payment()

    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def Complate(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request, 'Your payment Coplated successfully!')
            return HttpResponseRedirect(reverse('paymentApp:purchase', kwargs={'val_id':val_id, 'tran_id':tran_id}))

        if status == 'FAILED':
            messages.warning(request, 'Your payment Do not Coplated successfully! Try again')


    return render(request, 'paymentApp/complate.html', context={})


@login_required
def Purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered=True
    order.orderId=orderId
    order.paymentId=val_id
    order.save()
    cart_item = Cart.objects.filter(user=request.user, purchase=False)
    for item in cart_item:
        productId = item.item.id
        product = Product.objects.get(id=productId)
        quantity = item.quantity
        product.product_quintity = product.product_quintity - quantity
        product.save()
        item.purchase = True
        item.save()
    return HttpResponseRedirect(reverse("homeApp:home"))



