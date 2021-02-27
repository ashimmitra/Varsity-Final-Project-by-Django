from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def authlogin(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('student.profile')
        else:    
            messages.error(request, 'ই-মেইল অথবা পাসওয়ার্ড ভুল!')
    return render(request,'authentication/login.html')

def authregistration(request):
    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')

def userlogout(request):
    logout(request)
    messages.success(request, 'সফলভাবে !')
    return redirect('login')

