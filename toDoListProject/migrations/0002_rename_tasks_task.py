# Generated by Django 5.0.3 on 2024-03-29 15:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDoListProject', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
