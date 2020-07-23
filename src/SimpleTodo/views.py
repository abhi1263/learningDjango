from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tasks


# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, './SimpleTodo/task_listing.html', context)


def add_task(request):
    if request.method == "POST":
        new_task = request.POST['newTask']
        Tasks.objects.create(task_title=new_task)
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


def edit_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    context = {
        'task': task
    }
    return render(request, './SimpleTodo/edit_task.html', context)


def save_edit_task(request, task_id):
    if request.method == "POST":
        tasks = get_object_or_404(Tasks, pk=task_id)
        tasks.task_title = request.POST['newTaskTitle']
        tasks.save()
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


def delete_task(request,  task_id):
    return HttpResponse("Task deleted")
