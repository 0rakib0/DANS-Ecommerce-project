from django.urls import path
from . import views
app_name = 'paymentApp'
urlpatterns = [
    path('chckout-order/', views.Checkout, name='checkout'),
    path('payment/', views.Payment, name='payment'),
    path('status/', views.Complate, name='complate'),
    path('purchase/<val_id>/<tran_id>/', views.Purchase, name='purchase'),
    
]
