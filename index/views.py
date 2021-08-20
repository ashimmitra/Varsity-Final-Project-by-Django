from django.shortcuts import render
from .models import AboutSite
from .models import Slider
from .models import Contact
from .models import Notice
from .models import Books

def home(request):
    aboutdata = AboutSite.objects.all()[0]
    sliderdata = Slider.objects.all()
    context = {
        'AboutSite': aboutdata,
        'Slider': sliderdata
    }
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactdata = Contact(name=name,email=email,subject=subject,message=message)
        contactdata.save()
    return render(request,"index.html",context)

def notice(request):
    notices = Notice.objects.all()
    return render(request,"notice.html",{'notices':notices})

def classes(request):
    return render(request, 'classes.html')

def books(request):
    book_list = Books.objects.all()
    return render(request, 'books.html',{'book_list':book_list})
