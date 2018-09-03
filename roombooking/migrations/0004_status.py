# Generated by Django 2.1 on 2018-09-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0003_booking_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance', models.CharField(choices=[('TF', 'Teacher Fazilawati'), ('TA', 'Teacher Ar'), ('RR', '3R room')], max_length=2)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]