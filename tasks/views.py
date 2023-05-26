from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


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


class CloseOpenTask(View):
    def post(self, request, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        if task.is_completed is False:
            task.is_completed = True
            task.save()
        else:
            task.is_completed = False
            task.save()
        return HttpResponseRedirect(
            reverse_lazy("tasks:task-list")
        )


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
