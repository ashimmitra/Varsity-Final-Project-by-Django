
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='holome'),
    path('blog/', views.blog, name='blog'),
]
