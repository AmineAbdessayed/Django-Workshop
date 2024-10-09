# Generated by Django 4.1 on 2024-10-09 14:22

import Event.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('state', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('M', 'Musique'), ('C', 'Cinema'), ('S', 'Sport')], max_length=1)),
                ('evt_date', models.DateTimeField()),
                ('email', models.EmailField(max_length=254, validators=[Event.models.verifEmail])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='participation_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation_date', models.DateField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.event')),
            ],
        ),
    ]