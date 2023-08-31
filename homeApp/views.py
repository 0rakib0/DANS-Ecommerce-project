from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopApp.models import Product, WishList, Category, Banner1, Banner2

# Create your views here.

def index(request):
    newProduct = Product.objects.filter(is_newarival=True)
    featuredProduct = Product.objects.filter(is_featured=True)
    firstBanner = Banner1.objects.all()
    secondBanner = Banner2.objects.get(id=1)
    
    searResultTitle = None
    productName = None
    productCode = None
    if request.method == 'GET':
        searValue = request.GET.get('search')
    if searValue:
        searResultTitle = Product.objects.filter(roduct_title__icontains=searValue)
        productName = Product.objects.filter(product_name__icontains=searValue)
        productCode = Product.objects.filter(product_code__icontains=searValue)
    
    
    context = {
        'searResultTitle':searResultTitle,
        'productName':productName,
        'productCode':productCode,
        'newProduct':newProduct,
        'featuredProduct':featuredProduct,
        'firstBanner':firstBanner,
        'secondBanner':secondBanner
    }
    return render(request, 'homeApp/home.html', context)
