from django.shortcuts import render
from 

def home(request):
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
