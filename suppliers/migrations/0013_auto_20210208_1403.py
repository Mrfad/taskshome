# Generated by Django 3.1.6 on 2021-02-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0012_car_carmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='car',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='CarModel',
        ),
    ]