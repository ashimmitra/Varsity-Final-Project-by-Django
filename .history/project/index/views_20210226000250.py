from django.shortcuts import render
from .models im

def home(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
