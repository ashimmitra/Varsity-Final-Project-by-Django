from django.shortcuts import render,re
from django.contrib.auth import authentication.login

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')

