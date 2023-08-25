from django.urls import path
app_name = 'homeApp'
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Dance-online-shop/', views.Base, name='base')
]
