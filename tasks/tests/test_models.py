import datetime

from django.test import TestCase

from tasks.models import Tag, Task


class ModelsTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test")
        self.assertEqual(str(tag), "Test")

    def test_ordering_tasks(self):
        Task.objects.all().delete()
        first_task = Task.objects.create(
            description="First",
            creation_date=datetime.date(2023, 7, 1),
            is_completed=False,
        )
        second_task = Task.objects.create(
            description="Second",
            creation_date=datetime.date(2023, 7, 2),
            is_completed=False,
        )
        third_task = Task.objects.create(
            description="Third",
            creation_date=datetime.date(2023, 7, 1),
            is_completed=True,
        )
        task_list = Task.objects.all()

        self.assertEqual(task_list.first(), first_task)
        self.assertEqual(task_list[1], second_task)
        self.assertEqual(task_list.last(), third_task)
