from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag

TASK_LIST_URL = reverse_lazy("tasks:task-list")
TAG_LIST_URL = reverse_lazy("tasks:tag-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = TASK_LIST_URL


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = TASK_LIST_URL


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = TASK_LIST_URL


class CloseOpenTask(View):
    def post(self, request, **kwargs):
        task = Task.objects.get(id=kwargs["pk"])
        if task.is_completed is False:
            task.is_completed = True
            task.save()
        else:
            task.is_completed = False
            task.save()
        return HttpResponseRedirect(TASK_LIST_URL)


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = TAG_LIST_URL


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = TAG_LIST_URL


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = TAG_LIST_URL
