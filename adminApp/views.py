from django.shortcuts import render
from shopApp.models import Product, Category
# Create your views here.
def Dashbord(request):
    context = {
        
    }
    return render(request, 'AdminDashbord/dashbord.html', context)
def addProduct(request):
    category = Category.objects.all()
    if request.method == 'POST':
        productName = request.POST.get('product-name')
        productCode = request.POST.get('product-code')
        categoryId = request.POST.get('categoryId')
        quantity = request.POST.get('quantity')
        productTitle = request.POST.get('product-title')
        image = request.FILES.get('image')
        colorImage = request.FILES.getlist('color-image')
        productDetails = request.POST.get('product-details')
        regularPrice = request.POST.get('regular-price')
        isDiscount = request.POST.get('isDiscount')
        discountPrice = request.POST.get('discount-price')
        isNew = request.POST.get('isNew')
    context = {
        'category':category
    }    
    return render(request, 'AdminDashbord/add-product.html', context)