
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('blog/', views.blog, name='blog'),
    path('student/',include('student.urls')),
]
