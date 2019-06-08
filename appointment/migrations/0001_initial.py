# Generated by Django 2.2 on 2019-04-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id_number', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('department', models.CharField(blank=True, max_length=30)),
                ('position', models.CharField(choices=[('S', 'Students'), ('T', 'Teachers'), ('A', 'Admins')], default='S', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=80)),
                ('start_time', models.DateTimeField(unique=True)),
                ('end_time', models.DateTimeField(unique=True)),
                ('rooom', models.CharField(choices=[('1', 'Cg. Fazilawati'), ('2', 'Cg Ainul'), ('3', 'Bilik 3R')], default='3', max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.User')),
            ],
        ),
    ]