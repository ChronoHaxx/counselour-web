# Generated by Django 2.1 on 2018-09-04 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdb', '0006_student_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(default='2', max_length=3),
        ),
    ]