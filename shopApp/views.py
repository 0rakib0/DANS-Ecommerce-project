from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def Products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products':products,
        'category':category
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