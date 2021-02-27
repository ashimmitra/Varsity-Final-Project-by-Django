from django.shortcuts import render
from .s import AboutSite

def home(request):
    aboutdata=AboutSite.objects.all()
    context=[
        'about'=aboutdata
    ]
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 
