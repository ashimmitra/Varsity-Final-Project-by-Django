from django.shortcuts import render

def login(request):
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/login.html')

def forgotpassword(request):
    return render(request,'authentication/login.html')

