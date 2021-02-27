
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('student/',include('student.urls')),
]
