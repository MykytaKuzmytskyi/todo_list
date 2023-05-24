from django.shortcuts import render
from django.views import generic

from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"
