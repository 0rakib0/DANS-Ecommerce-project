from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('registration-form/', views.Account, name='registration'),
    path('register/', views.Regitration, name='register'),
    path('login-form/', views.loginForm, name='login_form'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.User_logout, name='logout'),
    path('profile/', views.User_Profile, name='profile'),
    path('change-password/', views.chnagePassword, name='change_pass'),
    path('Forget-User-password/', views.forgetPassword, name='forgetPass')
]
