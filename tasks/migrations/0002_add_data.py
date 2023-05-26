from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'fixture_data.json', app_label='tasks')


def reverse_func(apps, schema_editor):
    print('reverse')


class Migration(migrations.Migration):
    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_func),
    ]
