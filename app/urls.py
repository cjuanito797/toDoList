from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'app'

urlpatterns = [
    path ('', views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path ('register/', views.register, name='register'),
    path('newlist/', views.new_list, name='new_list'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('newTask/', views.addNewTask, name='addNewTask'),
    path ('<int:pk>/delete', views.deleteList, name='deleteList'),

]
