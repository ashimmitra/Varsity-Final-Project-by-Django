from django.shortcuts import render,redirect
from django.contrib.auth import au,login

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authentication()
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')

