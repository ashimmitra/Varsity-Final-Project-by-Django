from django.shortcuts import render
from django.http import HttpResponse


def student(request):
    return HttpResponse("this is student page")

def profile(request):
    return render("this is student's profile page")
