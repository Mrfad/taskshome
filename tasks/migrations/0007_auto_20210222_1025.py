# Generated by Django 3.1.6 on 2021-02-22 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20210222_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskpriority',
            options={'verbose_name': 'Task Priority', 'verbose_name_plural': 'Tasks Priority'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='rest_amount',
        ),
    ]
