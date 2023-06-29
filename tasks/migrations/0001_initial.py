# Generated by Django 4.1.5 on 2023-05-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField(null=True, blank=True,)),
                ('is_completed', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tasks', to='tasks.tag')),
            ],
            options={
                'ordering': ['is_completed', '-creation_date'],
            },
        ),
    ]
