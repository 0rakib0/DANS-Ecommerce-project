from django.shortcuts import render, redirect
from shopApp.models import Product, Category, ColorImage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def Dashbord(request):
    context = {
        
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
        productDetails = request.POST.get('product-details')
        regularPrice = request.POST.get('regular-price')
        isDiscount = request.POST.get('isDiscount')
        discountPrice = request.POST.get('discount-price')
        isNew = request.POST.get('isNew')        
        gategory = Category.objects.get(id=categoryId)
        
        # for image in colorImage:
        #     uploaded_image = UploadedImage(image=image)
        #     uploaded_image.save()
        
        product = Product(
            product_name = productName,
            product_code = productCode,
            product_quintity = quantity,
            product_category = gategory,
            roduct_title = productTitle,
            image = image,
            color_name = colorName,
            details = productDetails,
            main_price = regularPrice,            
            dic_price = discountPrice
        )
        if isNew == 'on':
            product.is_newarival = True
        if isDiscount == 'on':
            product.is_discount = True
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