from django.contrib import admin
from django.urls import path, include
from base import urls,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'), name='home'),
]
