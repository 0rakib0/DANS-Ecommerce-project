from django.shortcuts import render, redirect
from .models import Category, Product, WishList
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Products(request):
    selectedProduct = None
    products = Product.objects.all()
    category = Category.objects.all()
    if request.method == 'GET':
        CategoryId = request.GET.get('category')
    if CategoryId != '--SELET CATEGORY--':   
        selectedProduct = Product.objects.filter(product_category=CategoryId)
    

    
    context = {
        'products':products,
        'category':category,
        'selectedProduct':selectedProduct
    }
    return render(request, 'shopApp/shop.html', context)

def ProductDetails(request, slug):
    singProduct = Product.objects.get(slug=slug)
    categoryId = singProduct.product_category.id
    reletedProduct = Product.objects.filter(product_category=categoryId)
    context = {
        'singProduct':singProduct,
        'reletedProduct':reletedProduct
    }
    return render(request, 'shopApp/viewProduct.html', context)
@login_required
def ViewWishList(request):
    wish_List = WishList.objects.filter(user=request.user)
    context = {
        'wish_List':wish_List
    }
    return render(request, 'shopApp/wishlist.html', context)
@login_required
def AddWishList(request, slug):
    product = Product.objects.get(slug = slug)
    wishlist = WishList.objects.filter(product=product)
    print(wishlist)
    if product:
        if wishlist:
            messages.success(request, 'Product already in wish list')
            return redirect('shopApp:wishList')
        else:
            addWishList = WishList(
                product = product,
                user = request.user
            )
            addWishList.save()
            messages.success(request, 'Product Successfully added in wish list!')
            return redirect('shopApp:wishList')
    else:
        messages.warning(request, 'Product not add to wish list!')
        return redirect('shopApp:wishList')
@login_required
def RemoveWishList(request, id):
    wish_list = WishList.objects.get(id=id)
    if wish_list:
        wish_list.delete()
        messages.success(request, 'Product successfully removed!')
        return redirect('shopApp:wishList')
    else:
        messages.success(request, 'Product not removed! somethink wrong!')
        return redirect('shopApp:wishList')
