from django.shortcuts import render

# Create your views here.


def Checkout(request):
    context={
        
    }
    return render(request, 'paymentApp/checkout.html', context)