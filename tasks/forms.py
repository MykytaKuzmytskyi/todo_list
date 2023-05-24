from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Task
        fields = ("description", "tags", "deadline")
