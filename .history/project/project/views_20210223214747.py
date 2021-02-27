from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home page")

def student(request):
    return HttpResponse("this is student page")    

def blog(request):
    return HttpResponse("this is blog page")    