# Generated by Django 2.2 on 2019-05-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_appointment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='slug',
        ),
    ]
