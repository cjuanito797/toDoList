from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('newList', views.new_list, name='new_list'),
]