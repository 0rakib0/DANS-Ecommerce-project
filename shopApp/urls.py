from django.urls import path
from . import views
app_name = 'shopApp'

urlpatterns = [
    path('product-shop/', views.Products, name='products'),
    path('view-product-detals/<slug>/', views.ProductDetails, name='productDetails'),
]
