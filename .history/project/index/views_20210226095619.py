from django.shortcuts import render
from .models import AboutSite
from .models import Slider

def home(request):
    aboutdata = AboutSite.objects.all()[0]
    sliderdata = Slider.objects.all()[0]
    context = {
        'AboutSite': aboutdata,
        'AboutSite': aboutdata,
    }
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 
