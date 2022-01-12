from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    # path('deleteTodo/', views.deleteTodo, name='deleteTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo'),
    path('reTodo/', views.reTodo, name='reTodo'),
]