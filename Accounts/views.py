from django.shortcuts import render, redirect
from .models import User, Profile
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from orderApp.models import Order
# Create your views here.


def Account(request):
    return render(request, 'accountApp/register.html')


def Regitration(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email=email).first():
            messages.warning(request, 'Email Already exist!')
            return redirect('accounts:register')
        if password1 != password2:
            messages.warning(request, 'Password not match!')
            return redirect('accounts:register')
        else:  
            mk_pass = make_password(password1)
            user = User (
                email = email,
                password = mk_pass
            )
            user.save()
            messages.success(request, 'Your Account Successfylly Created!')
            return redirect('accounts:login_form')
 
    return redirect('accounts:accounts')
    

def loginForm(request):
    return render(request, 'accountApp/login.html')


def User_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'Admin':
                return redirect('adminApp:dashbord')
            if user.user_type == 'Customer':
                return redirect('homeApp:home')
            return redirect('homeApp:home')
        else:
            messages.error(request, 'Email or password not valid!')
            return redirect('accounts:login_form')
    return redirect('homeAppp:home')
    
  

def User_logout(request):
    logout(request)
    return redirect('homeApp:home')


def User_Profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        addresd1 = request.POST.get('addresd1')
        profile_pic = request.FILES.get('profile_pic')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        profile = Profile.objects.get(user=user)
      
    
        profile.username = username
        profile.full_name = fullname
        profile.address_1 = addresd1
        if profile_pic is not None:
            profile.profile_pic = profile_pic
        profile.city = city
        profile.zipcode = zip_code
        profile.country = country
        profile.phone = phone
        profile.save()
        messages.success(request, 'Profile successfully updated!')
        return redirect('accounts:profile')   
    try: 
        orders = Order.objects.filter(user=request.user, ordered=True)
    except:
        messages.success(request, 'You DO not have Any active order!')
        return redirect('accounts:profile')
    
    context = {
        'profile':profile,
        'orders':orders,
    }
    if request.user.user_type == 'Admin':
        return render(request, 'accountApp/admin_profile.html', context)
    else:
        return render(request, 'accountApp/profile.html', context)
    
def chnagePassword(request):
    user_email = request.user.email
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_pass1 = request.POST.get('new_pass1')
        new_pass2 = request.POST.get('new_pass2')
        
        user = authenticate(username=user_email, password=old_password)
        if user is not None:
            if new_pass1 != new_pass2:
                messages.success(request, 'new password and confirm new password not same!')
                return redirect('accounts:profile')
            else:
                user.set_password(new_pass1)
                user.save()
                messages.success(request, 'Password Changed.Please Login!')
                return redirect('accounts:logout')
        else:
            messages.success(request, 'Old Password Not Correct!')
            return redirect('accounts:profile')
    else:
        messages.success(request, 'Action not complate. Somethink wrong!')
        return redirect('accounts:profile')
    
    
def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        newPassword = request.POST.get('newPassword')
        user = User.objects.filter(email=email).first()
        if user:
            user_name = user.profile.username
            if user_name == username:
                user.set_password(newPassword)
                user.save()
                messages.success(request, 'New Password Set. Try to Login!')
                return redirect('accounts:login_form')
            else:
                messages.success(request, 'User Not Found with this username!')
                return redirect('accounts:login_form')
        else:
            messages.success(request, 'User Not Found!')
            return redirect('accounts:login_form')
        
    return render(request, 'accountApp/forgetPass.html')