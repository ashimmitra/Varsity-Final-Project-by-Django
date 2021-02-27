
from django.urls import path
from .import views

urlpatterns = [
    path('', views.authlogin, name='login'),
    path('registration/', views.registration, name='registration'),
    path('forgot-password/', views.forgotpassword, name='forgotpassword'),
]
