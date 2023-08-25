from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopApp.models import Product

# Create your views here.
def Base(request):
    return render(request, 'base.html')


def index(request):
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
        'productCode':productCode
    }
    return render(request, 'homeApp/home.html', context)
