from django.shortcuts import render



def student(request):
    return HttpResponse("this is student page")

def profile(request):
    return HttpResponse("this is student's profile page")
