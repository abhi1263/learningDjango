from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tasks


# to display all task listing
def index(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, './SimpleTodo/task_listing.html', context)


# to add task
def add_task(request):
    if request.method == "POST":
        new_task = request.POST['newTask']
        tasks = Tasks(task_title=new_task)
        tasks.save()
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


# to edit task
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    context = {
        'task': task
    }
    return render(request, './SimpleTodo/edit_task.html', context)


# save the edit changes
def save_edit_task(request, task_id):
    if request.method == "POST":
        tasks = get_object_or_404(Tasks, pk=task_id)
        tasks.task_title = request.POST['newTaskTitle']
        tasks.save()
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


# delete task
def delete_task(request,  task_id):
    tasks = get_object_or_404(Tasks, pk=task_id)
    tasks.delete()
    return HttpResponseRedirect(reverse('SimpleTodo:index'))


# change the status of the task('completed' or 'pending')
def update_task_status(request, task_id):
    tasks = get_object_or_404(Tasks, pk=task_id)
    if request.method == "GET":
        if tasks.task_status:
            tasks.task_status = False
        else:
            tasks.task_status = True
        tasks.save()
    return HttpResponseRedirect(reverse('SimpleTodo:index'))

