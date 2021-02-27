from django.shortcuts import render
from .model import 

def home(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
