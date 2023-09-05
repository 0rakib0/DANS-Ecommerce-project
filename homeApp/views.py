from django.shortcuts import render, redirect
from django.http import HttpResponse
from shopApp.models import Product, WishList, Category, Banner1, Banner2
from django.contrib import messages
from .models import Massage

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

def ContactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messagee = request.POST.get('message')

        msg = Massage(
            name = name,
            email = email,
            message = messagee
        )
        msg.save()
        messages.success(request, 'Messege Successfully Send!')
        return redirect('homeApp:contact_us')
    return render(request, 'homeApp/contact.html', context={})


def AboutUS(request):
    return render(request, 'homeApp/about.html')


def Tearm(request):
    return render(request, 'homeApp/tearm.html')


def FAQ(request):
    
    return render(request, 'homeApp/FAQ.html')