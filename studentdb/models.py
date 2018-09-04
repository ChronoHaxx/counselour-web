from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    batch = models.CharField(max_length=1, default='4')
    student_class = models.CharField(max_length=3)
    no_kp = models.CharField(max_length=6, unique=True, primary_key=True)
    homeroom = models.CharField(max_length = 50)
    child_no = models.CharField(max_length=10)
    siblings = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    no_ic = models.CharField(max_length=11,default='021313213')

    def __str__(self):
        return self.name
