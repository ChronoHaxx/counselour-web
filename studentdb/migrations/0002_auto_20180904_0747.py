# Generated by Django 2.1 on 2018-09-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='child_no',
            field=models.CharField(default=4, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='ic',
            field=models.CharField(default=313131, max_length=11, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=12321425342, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='siblings',
            field=models.CharField(default=5, max_length=10),
            preserve_default=False,
        ),
    ]
