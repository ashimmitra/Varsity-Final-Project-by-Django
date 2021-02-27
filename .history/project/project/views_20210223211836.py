from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")    