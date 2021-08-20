from django.shortcuts import render
from django.http import HttpResponse


def student(request):
    return HttpResponse("this is student page")

def profile(request):
    return render(request,'student/profile.html')
