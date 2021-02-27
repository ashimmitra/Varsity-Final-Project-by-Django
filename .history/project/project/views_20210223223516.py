from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return re("this is home page")

def blog(request):
    return HttpResponse("this is blog page")    