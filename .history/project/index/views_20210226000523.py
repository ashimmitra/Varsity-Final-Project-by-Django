from django.shortcuts import render
from .model import AboutSite

def home(request):
    aboutdata=AboutSite.objects.all()
    context=[
        'about'=aboutdata
    ]
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 
