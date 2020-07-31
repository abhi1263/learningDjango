from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SimpleTodo'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/add', views.add_task, name='add_task'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/change_status', views.update_task_status, name='update_task_status'),

    path('user/register', views.user_register, name='user_register'),
    path('user/login', views.user_login, name='user_login'),
    path('user/logout', views.user_logout, name='user_logout')
]
