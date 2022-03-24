from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'app'

urlpatterns = [
    path ('', auth_views.LoginView.as_view ( ), name='user_login'),
    path ('home/', views.home, name='home'),
    path ('register/', views.register, name='register'),
    path('newlist/', views.new_list, name='new_list'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('newTask/', views.addNewTask, name='addNewTask')

]
