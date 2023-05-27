import datetime

from django.test import TestCase
from django.urls import reverse_lazy

from tasks.models import Tag, Task


class FormsTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="Test")
        self.task = Task.objects.create(
            description="Test",
        )
        self.task.tags.add(self.tag)

    def test_create_task(self):
        response = self.client.post(
            reverse_lazy("tasks:task-create"),
            {
                "description": "Test",
                "tags": [self.tag.id],
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_update_task(self):
        tag_1 = Tag.objects.create(name="First")

        response = self.client.post(
            reverse_lazy("tasks:task-update", kwargs={"pk": self.task.id}),
            {
                "pk": self.task.id,
                "description": "Test description",
                "tags": [tag_1.id],
            },
        )
        Task.objects.get(id=self.task.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Task.objects.get(id=self.task.id).description,
            "Test description"
        )

    def test_delete_task(self):
        response = self.client.post(
            reverse_lazy("tasks:task-delete", kwargs={"pk": self.task.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_tag_create(self):
        response = self.client.post(
            reverse_lazy("tasks:tag-create"), {"name": "Test_tag"}
        )
        self.assertEqual(response.status_code, 302)

    def test_update_tag(self):
        response = self.client.post(
            reverse_lazy("tasks:tag-update", kwargs={"pk": self.tag.id}),
            {
                "pk": self.tag.id,
                "name": "Second",
            },
        )
        Tag.objects.get(id=self.tag.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.get(id=self.tag.id).name, "Second")

    def test_delete_tag(self):
        response = self.client.post(
            reverse_lazy("tasks:tag-delete", kwargs={"pk": self.tag.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())

    def test_validate_deadline(self):
        future = datetime.date(2035, 1, 1)
        past = datetime.date(2000, 1, 1)

        response = self.client.post(
            reverse_lazy("tasks:task-create"),
            {
                "description": "future_task",
                "tags": [self.tag.id],
                "deadline": future,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Task.objects.filter(description="future_task").exists()
        )

        response = self.client.post(
            reverse_lazy("tasks:task-create"),
            {
                "description": "past_task",
                "tags": [self.tag.id],
                "deadline": past,
            },
        )
        self.assertFalse(Task.objects.filter(description="past_task").exists())
