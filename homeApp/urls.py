from django.urls import path
app_name = 'homeApp'
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Contact-Us/', views.ContactUs, name='contact_us'),
    path('about-us/', views.AboutUS, name='about_us'),
    path('tearn-&-condition/', views.Tearm, name='tearm'),
    path('FAQ/', views.FAQ, name='faq'),

]
