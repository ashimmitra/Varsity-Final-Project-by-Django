
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
      path('blog/', views.blog, name='blog'),
    path('profile/', views.profile, name='student.profile'),
]
