# Generated by Django 4.0.3 on 2022-03-04 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_list_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='item',
            field=models.ManyToManyField(to='app.item'),
        ),
    ]
