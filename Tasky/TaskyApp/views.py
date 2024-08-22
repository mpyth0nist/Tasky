from django.shortcuts import render

from .forms import *
from django.db import IntegrityError, connection
from django.conf import settings

tasks = []

tasks_num = len(tasks)

def index(request):
    return render(request, "TaskyApp/index.html")

def view(request):
    return render(request, "TaskyApp/view.html", {'tasks_num':tasks_num, 'tasks': tasks})

def add(request):

    
    if request.method == 'POST':
        form = Todolist(request.POST)

        if form.isvalid():

            task = form.cleaned_data["task"]
            task_priority = form.cleaned_data["task_priority"]

            tasks.append([task, task_priority])

            
    else:
        form = Todolist()

    return render(request, "TaskyApp/add.html",{"form": Todolist()})


