from django.urls import path
from . import views
app_name = 'orderApp'

urlpatterns = [
    path('add-to-card/<slug>/', views.addToCard, name='add_to_card'),
    path('product-cart-view/', views.cardView, name='card_view'),
    path('remove-card-item/<slug>/', views.removeCardItem, name='remove_card'),
    path('quantity-incease/<slug>/', views.IncreaseQuintity, name='quantity_increase'),
    path('quantity-decrease/<slug>/', views.DecreaseQuanity, name='quantity_decrease'),
]
