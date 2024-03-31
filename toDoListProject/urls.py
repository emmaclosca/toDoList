from django.urls import path
from .views import Tasks, TaskDetail, AddTask, UpdateTask, DeleteTask, UserLogin, UserSignUp
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('addTask/', AddTask.as_view(), name='addTask'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='taskDetail'),
    path('updateTask/<int:pk>/', UpdateTask.as_view(), name='updateTask'),
    path('deleteTask/<int:pk>/', DeleteTask.as_view(), name='deleteTask'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', UserSignUp.as_view(), name='signup'),
]