from django.shortcuts import render
from .models import AboutSite
from .models import Slider
from .models import Contact

def home(request):
    aboutdata = AboutSite.objects.all()[0]
    sliderdata = Slider.objects.all()
    context = {
        'AboutSite': aboutdata,
        'Slider': sliderdata
    }
    if request.METHOD 
    return render(request,"index.html",context)

def blog(request):
    return render(request,"blog.html") 
