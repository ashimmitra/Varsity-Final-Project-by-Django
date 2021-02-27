from django.shortcuts import render
from django

def home(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
