# Generated by Django 4.0.3 on 2022-03-04 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_ugency_level_item_urgency_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='item',
        ),
    ]