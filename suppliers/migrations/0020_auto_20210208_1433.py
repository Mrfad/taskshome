# Generated by Django 3.1.6 on 2021-02-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0019_supplier_supplier_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier_person',
            old_name='contact_person',
            new_name='company',
        ),
        migrations.AddField(
            model_name='supplier_person',
            name='contact_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]