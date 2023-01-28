from django.http import response, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):

    return render(request, "index.html")

def signin(request):
    
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)

        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.error(request,"login failled. Something went wrong")
            return redirect ('/signin')
    return render(request, "signin.html")
          
def signup(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        my_user=User.objects.create_user(username,email,password)
        my_user.save() 
        messages.success(request, "account created successfully. You can login here.")
        return redirect("signin")
    return render(request, "signup.html")

def home(request):
    return render(request, "home.html")