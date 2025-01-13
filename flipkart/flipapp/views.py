from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        first_name=request. POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pword']
        username=request.POST['uname']
        user= User.objects.create_user(
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pword']
        user=authenticate(
            request,username=username,password=password
        )
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            err='username and password doesnt match'
            return render(request,'login.html',{'err':err})
    else:
        return render(request,'login.html')
    
def user_logout(request):
    logout(request)
    return redirect('login')

 

