# Generated by Django 3.1.6 on 2021-02-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0006_auto_20210205_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
