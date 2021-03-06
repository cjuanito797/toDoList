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
    path('<int:pk>/newTask/', views.create_item_model_form, name='create_item_model_form'),
    path ('<int:pk>/delete', views.deleteList, name='deleteList'),
    path('<int:pk>/complete', views.completeItem, name='completeItem'),

]
