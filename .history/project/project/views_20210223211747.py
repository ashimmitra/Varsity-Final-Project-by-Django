from django.http import


def home(request):
    return HttpResponse("this is home page")