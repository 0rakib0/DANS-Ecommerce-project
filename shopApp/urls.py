from django.urls import path
from . import views
app_name = 'shopApp'

urlpatterns = [
    path('product-shop/', views.Products, name='products'),
    path('view-product-detals/<slug>/', views.ProductDetails, name='productDetails'),
    path('wish-list/', views.ViewWishList , name='wishList'),
    path('add-product-wishlist/<slug>/', views.AddWishList, name='addWishList'),
    path('remove-wishlist-item/<int:id>/', views.RemoveWishList, name='removewishlist' ),
]