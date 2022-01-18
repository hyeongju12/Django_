from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SignupView.views, name='SignupView'),
    path('email/', views.email, name='signup_email')
]