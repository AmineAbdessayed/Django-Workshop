# Generated by Django 4.1 on 2024-10-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='nbr_participant',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
