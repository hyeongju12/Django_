from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginView, name='main_loginView'),
    path('index/', views.index, name='main_index'),
    path('login/', views.login, name='main_login'),
    path('logout/', views.logout, name='main_logout'),
    path('index/download/', views.download, name='main_download'),
]