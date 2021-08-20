
from django.urls import path
from .import views

urlpatterns = [
    path('', views.english),
    #path('',views.welcome),
    path('result/',views.result, name='result'),
    path('english/', views.english, name='profile.english'),
    path('bangla/', views.ban, name='profile.ban'),
    path('science/', views.science, name='profile.science'),
    path('math/', views.math, name='profile.math'),
    #path('ict/', views.ict, name='profile.ict'),
    path('icts/', views.icts, name='profile.icts'),
    path('mental-ability/', views.mental_ability, name='profile.mental_ability'),
    path('generalknowledge/', views.generalknowledge, name='profile.generalknowledge'),
]
