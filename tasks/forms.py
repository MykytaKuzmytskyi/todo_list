import datetime

from django import forms
from django.core.exceptions import ValidationError

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.SelectDateWidget, required=False)

    class Meta:
        model = Task
        fields = ("description", "tags", "deadline")

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline is not None and deadline < datetime.date.today():
            raise ValidationError(
                "The date cannot be in the past!"
            )
        return deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
