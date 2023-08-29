from django.urls import path
from . import views
app_name = 'adminApp'
urlpatterns = [
    path('Admin-Dashbord/', views.Dashbord, name='dashbord'),
    #-----------------> product <--------------------------
    path('add-product/', views.addProduct, name='add_product'),
    path('view-product-list/', views.viewProduct, name='view_product'),
    path('delet-product/<slug>/', views.deleteProduct, name='delete_product'),
    # ------------------> Category <-------------------------
    path('add-category/', views.addCategory, name='add_category'),
    path('view-category/', views.viewCategory, name='view_category'),
    path('delete-category/<int:id>/', views.deleteCategory, name='delete_category'),
    
]
