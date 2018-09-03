from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    student_class = models.CharField(max_length=3)
    no_kp = models.CharField(max_length=6, unique=True, primary_key=True)
    homeroom = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
        
