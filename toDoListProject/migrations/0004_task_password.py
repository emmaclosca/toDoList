# Generated by Django 5.0.3 on 2024-03-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoListProject', '0003_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
