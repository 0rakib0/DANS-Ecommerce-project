from django.urls import path
from . import views
app_name = 'paymentApp'
urlpatterns = [
    path('chckout-order/', views.Checkout, name='checkout'),
    
]
