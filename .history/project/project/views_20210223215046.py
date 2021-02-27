from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home page")


def blog(request):
    return HttpResponse("this is blog page")    