from django.shortcuts import render

# Create your views here.
def Dashbord(request):
    context = {
        
    }
    return render(request, 'AdminDashbord/dashbord.html', context)
