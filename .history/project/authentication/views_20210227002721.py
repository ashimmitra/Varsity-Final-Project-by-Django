from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['name']
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')

