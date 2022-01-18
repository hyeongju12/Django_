from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView, name='LoginView'),
    path('index/', views.index, name='main_index')
]