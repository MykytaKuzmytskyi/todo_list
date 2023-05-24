from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


def closing_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_completed is False:
        task.is_completed = True
        task.save()
    return HttpResponseRedirect(
        reverse_lazy("tasks:task-list")
    )
