from django.urls import path
from . import views
app_name = 'adminApp'
urlpatterns = [
    path('Admin-Dashbord/', views.Dashbord, name='dashbord'),
    path('add-product/', views.addProduct, name='add_product')
]
