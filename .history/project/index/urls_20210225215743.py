
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name=),
    path('blog/', views.blog, name='blog'),
    path('profile/', views.profile, name='student.profile'),
]
