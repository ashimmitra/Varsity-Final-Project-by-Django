from django.shortcuts import render
from .models import AboutSite

def home(request):
    aboutdata = AboutSite.objects.all()
    context={
        'AboutSite'=aboutdata,
    }
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 
