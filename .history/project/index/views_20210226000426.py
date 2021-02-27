from django.shortcuts import render
from .model import AboutSite

def home(request):
    aboutdata=AboutSitex = object()
    print(dir(x))
    return render(request,"index.html")

def blog(request):
    return render(request,"blog.html") 
