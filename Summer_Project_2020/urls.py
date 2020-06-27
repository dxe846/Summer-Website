"""
Definition of urls for Summer_Project_2020.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [

  
 

 
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

]