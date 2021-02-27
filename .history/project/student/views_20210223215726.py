from django.http import HttpResponse


def student(request):
    return HttpResponse("this is home page")

def blog(request):
    return HttpResponse("this is blog page")    