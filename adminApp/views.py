from django.shortcuts import render, redirect
from shopApp.models import Product, Category, ColorImage, Banner1, Banner2
from django.contrib.auth.decorators import login_required
from homeApp.models import Massage
from django.contrib import messages
from orderApp.models import Order, Cart
from Accounts.models import User
from paymentApp.models import Billing_Address
from datetime import timedelta, date
# Create your views here.
@login_required
def Dashbord(request):
    revenue = 0
    todayRevenue = 0
    client = User.objects.filter(user_type='Customer').count
    card = Cart.objects.filter(purchase = True)
    today = date.today()
    order = Order.objects.filter(createdAt=today)
    for i in order:
        total = i.getTotals()
        todayRevenue = todayRevenue + float(total)
    for i in card:
        total = i.get_total()
        revenue = revenue + float(total)
    context = {
        "client":client,
        'revenue':revenue,
        'order':order,
        'todayRevenue':todayRevenue
    }
    return render(request, 'AdminDashbord/dashbord.html', context)


@login_required
def viewProduct(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'AdminDashbord/view-product.html', context)


@login_required
def addProduct(request):
    color = None
    category = Category.objects.all()
    if request.method == 'POST':
        productName = request.POST.get('product-name')
        productCode = request.POST.get('product-code')
        categoryId = request.POST.get('categoryId')
        quantity = request.POST.get('quantity')
        productTitle = request.POST.get('product-title')
        image = request.FILES.get('image')
        colorImage = request.FILES.getlist('color-image')
        colorName = request.POST.get('color-name')
        size = request.POST.get('size')
        productDetails = request.POST.get('product-details')
        regularPrice = request.POST.get('regular-price')
        isDiscount = request.POST.get('isDiscount')
        discountPrice = request.POST.get('discount-price')
        isNew = request.POST.get('isNew')
        isFeatur = request.POST.get('isfeatured')    
        gategory = Category.objects.get(id=categoryId)
       
        
        product = Product(
            product_name = productName,
            product_code = productCode,
            product_quintity = quantity,
            product_category = gategory,
            roduct_title = productTitle,
            image = image,
            color_name = colorName,
            availableSize = size,
            details = productDetails,
            main_price = regularPrice,            
            dic_price = discountPrice
        )
        if isNew == 'on':
            product.is_newarival = True
        if isDiscount == 'on':
            product.is_discount = True
        if isFeatur == 'on':
            product.is_featured = True
        product.save()
        for color in colorImage:
            image = ColorImage(image=color)
            image.save()
            product.product_color_image.add(image)
        product.save()
        messages.success(request, 'Product SuccessFully Added!')
        return redirect('adminApp:add_product')
        
        
    context = {
        'category':category
    }    
    return render(request, 'AdminDashbord/add-product.html', context)

def deleteProduct(request, slug):
    product = Product.objects.get(slug=slug)
    if product:
        product.delete()
        messages.success(request, 'product Successfully Deleted!')
        return redirect('adminApp:view_product')
    else:
        messages.success(request, 'product not Deleted!')
        return redirect('adminApp:view_product')
    
    
def updateProduct(request, slug):
    product = Product.objects.get(slug=slug)
    
    if request.method == 'POST':
        productName = request.POST.get('product-name')
        productCode = request.POST.get('product-code')
        categoryId = request.POST.get('categoryId')
        quantity = request.POST.get('quantity')
        productTitle = request.POST.get('product-title')
        image = request.FILES.get('image')
        colorName = request.POST.get('color-name')
        size = request.POST.get('size')
        productDetails = request.POST.get('product-details')
        regularPrice = request.POST.get('regular-price')
        isDiscount = request.POST.get('isDiscount')
        discountPrice = request.POST.get('discount-price')
        isNew = request.POST.get('isNew')
        isFeatur = request.POST.get('isfeatured')      
        gategory = Category.objects.get(id=categoryId)
        
        product.product_name = productName
        product.product_code = productCode
        product.product_quintity = quantity
        product.product_category = gategory
        product.roduct_title = productTitle
        if image:
            product.image = image
        product.color_name = colorName
        product.availableSize = size
        product.details = productDetails
        product.main_price = regularPrice
        product.dic_price = discountPrice
        if isNew == 'on':
            product.is_newarival = True
        if isDiscount == 'on':
            product.is_discount = True
        if isFeatur == 'on':
            product.is_featured = True
        product.save()
        messages.success(request, 'Product Updated!')
        return redirect('adminApp:view_product')
    category = Category.objects.all()
    context = {
        'product':product,
        'category':category
    }
    return render(request, 'AdminDashbord/update-product.html', context)
    
    
# ------------------------------> Category <-------------------------------

def addCategory(request):
    if request.method == 'POST':
        categoryName = request.POST.get('category-name')
        category = Category(
            category_name=categoryName
        )
        category.save()
        messages.success(request, 'New Category Created!')
        return redirect('adminApp:add_category')
    return render(request, 'AdminDashbord/add-category.html')

def viewCategory(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'AdminDashbord/view-category.html', context)

def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    if category:
        category.delete()
        messages.success(request, 'Category Deleted!')
        return redirect('adminApp:view_category')
    else:
        messages.success(request, 'Category not Delete!')
        return redirect('adminApp:view_category')
def updateCategory(request, id):        
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        catName = request.POST.get('category-name')
        category.category_name = catName
        category.save()
        messages.success(request, 'Category Updated!')
        return redirect('adminApp:view_category')
    context = {
        'category':category
    }
    return render(request, 'AdminDashbord/cat-update.html', context)


# -------------------> Banner management<--------------------------
@login_required
def BannerFirst(request):
    if request.method == 'POST':
        offer_image = request.FILES.get('banner_pic')
        offer_name = request.POST.get('offer-name')
        offer_title = request.POST.get('offer_title')
        offer_Dis = request.POST.get('offer-description')

        banner = Banner1(
            offer_name = offer_name,
            offer_title = offer_title,
            offer_description = offer_Dis,
            banner_image = offer_image
        )
        banner.save()
        messages.success(request, 'Banner Added!')
        return redirect('adminApp:banner1')
    banner = Banner1.objects.all()
    return render(request, 'AdminDashbord/banner1.html', context={'banner':banner})


def FirstBannerDelete(request, id):
    baner = Banner1.objects.get(id=id)
    if baner:
        baner.delete()
        messages.success(request, 'Banner Deleted!')
        return redirect('adminApp:banner1')
    else:
        messages.success(request, 'Banner not Deleted!')
        return redirect('adminApp:banner1')

@login_required
def BannerSecond(request):
    if request.method == 'POST':
        offer_image = request.FILES.get('banner_pic')
        offer_name = request.POST.get('offer-name')
        offer_title = request.POST.get('offer_title')
        offer_Dis = request.POST.get('offer-description')
        
        benner = Banner2.objects.get(id=1)
        if offer_image:
            benner.banner_image = offer_image
        if offer_name:
            benner.offer_name = offer_name
        if offer_title:
            benner.offer_title = offer_title
        if offer_Dis:
            benner.offer_description = offer_Dis
        benner.save()
        messages.success(request, 'Banner Updated!')
        return redirect('adminApp:banner2')
    banner = Banner2.objects.all()
    return render(request, 'AdminDashbord/banner2.html', context={'banner':banner})


def ViewMassage(request):
    msg = Massage.objects.all()
    return render(request, 'AdminDashbord/msgView.html', context={'msg':msg})

def ReadStatus(request, id):
    msg = Massage.objects.get(id=id)

    msg.isRed = True
    msg.save()
    return redirect('adminApp:msg_view')

def msgDelete(request, id):
    msg = Massage.objects.get(id=id)
    if msg:
        msg.delete()
        messages.success(request, 'Massage Deleted!')
        return redirect('adminApp:msg_view')
    else:
        messages.success(request, 'Massage not deleted!')
        return redirect('adminApp:msg_view')
    
# ===================> view Customars Orders <==================
def orderList(request):
    all_orders = Order.objects.filter(ordered=True)
    context={
        'all_orders':all_orders,
    }
    return render(request, 'AdminDashbord/all-order.html', context)

def deliveryOrder(request):
    delivery_orders = Order.objects.filter(ordered=True, delivered_status=True)
    context = {
        'delivery_orders':delivery_orders,
    }
    return render(request, 'AdminDashbord/delivery-order.html', context)

def pendingOrder(request):
    pending_orders = Order.objects.filter(ordered=True, delivered_status=False)
    context = {
        'pending_orders':pending_orders,
    }
    return render(request, 'AdminDashbord/pending-order.html', context)


def Delete_order(request, id):
    order = Order.objects.get(id=id)
    try:
        order.delete()
        messages.success(request, 'Order Deleted!')
        return redirect('adminApp:all_order_list')
    except:
        messages.success(request, 'Order Not Deleted!')
        return redirect('adminApp:all_order_list')
    
def viewOrderInfo(request, id):
    order = Order.objects.get(id=id)
    order_user = order.user
    billing_info = Billing_Address.objects.get(user=order_user)
    context = {
        'order':order,
        'billing_info':billing_info
    }
    return render(request, 'AdminDashbord/view-order-info.html', context)

def DeliveryProduct(request, id):
    order = Order.objects.get(id=id)
    if order:
        order.delivered_status = True
        order.save()
        messages.success(request, 'Order Delivered!')
        return redirect('adminApp:deliver_order')
    else:
        messages.success(request, 'Order Not Delivered!')
        return redirect('adminApp:pending_order')


def AllSellReport(request):
    revenue = 0
    orders = Order.objects.filter(ordered=True)
    card = Cart.objects.filter(purchase = True)
    for i in card:
        total = i.get_total()
        revenue = revenue + float(total)
    context = {
        'orders':orders,
        'revenue':revenue
    }
    return render(request, 'AdminDashbord/orders_report.html', context)
   