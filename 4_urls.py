       # urls
       
from django.conf import settings
from django.contrib import admin
from django.urls import path
from views import views


urlpatterns = [
    path('', views.home)
]




