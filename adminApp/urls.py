from django.urls import path
from . import views
app_name = 'adminApp'
urlpatterns = [
    path('Admin-Dashbord/', views.Dashbord, name='dashbord'),
    #-----------------> product <--------------------------
    path('add-product/', views.addProduct, name='add_product'),
    path('view-product-list/', views.viewProduct, name='view_product'),
    path('delet-product/<slug>/', views.deleteProduct, name='delete_product'),
    path('update-product/<slug>/', views.updateProduct, name='update_product'),
    # ------------------> Category <-------------------------
    path('add-category/', views.addCategory, name='add_category'),
    path('view-category/', views.viewCategory, name='view_category'),
    path('delete-category/<int:id>/', views.deleteCategory, name='delete_category'),
    path('view category details/<id>/', views.updateCategory, name='update_category'),
    
    # --------------------> Banner management <---------------
    path('banner-update/', views.BannerFirst, name='banner1'),
    path('new-product-banner-update/', views.BannerSecond, name='banner2'),
    path('first-banner-delete/<id>/', views.FirstBannerDelete, name='first_banner_delete')
]
