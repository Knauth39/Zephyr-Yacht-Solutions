# Generated by Django 4.0.10 on 2023-02-21 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='publish',
        ),
    ]
