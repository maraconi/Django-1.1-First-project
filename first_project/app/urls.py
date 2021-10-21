from django.contrib import admin
from django.urls import path, include
from .views import home_view, time_view, workdir_view

urlpatterns = [
    path('', home_view, name='home'),
    path('time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir')
]