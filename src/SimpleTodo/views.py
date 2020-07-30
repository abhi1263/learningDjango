from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Tasks
from .forms import CreateUserForm


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
        new_task_title = request.POST['newTask']
        tasks = Tasks(task_title=new_task_title)
        tasks.save()
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


# to edit task
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    if request.method == "GET":
        ''' Fetches task object of the particular task and passes it to the form in the template '''
        context = {
            'task': task
        }
        return render(request, './SimpleTodo/edit_task.html', context)
    else:
        ''' Saves the changes to database after they are submitted by user  '''
        task.task_title = request.POST['newTaskTitle']
        task.save()
        return HttpResponseRedirect(reverse('SimpleTodo:index'))


# delete a task
def delete_task(request, task_id):
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


# User registration page
def user_register(request):
    if request.method == "GET":
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, './SimpleTodo/user_register.html', context)
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account created successfully')
            return HttpResponseRedirect(reverse('SimpleTodo:user_register'))
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return HttpResponseRedirect(reverse('SimpleTodo:user_register'))