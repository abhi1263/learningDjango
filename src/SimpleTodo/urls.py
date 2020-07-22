from django.contrib import admin
from django.urls import path
from . import views

app_name = 'SimpleTodo'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/add', views.add_task, name='add_task'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.edit_task, name='delete_task'),
]
