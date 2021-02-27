from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"index.ht")

def blog(request):
    return HttpResponse("this is blog page")    