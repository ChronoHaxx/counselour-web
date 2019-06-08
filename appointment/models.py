from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    objective = models.CharField(max_length=80)
    start_time = models.DateTimeField(unique=True)
    end_time = models.DateTimeField(unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

    FAZIL = '1'
    AINUL = '2'
    BILIK = '3'
    ROOM_CHOICES =(
        (FAZIL, 'Cg. Fazilawati'),
        (AINUL, 'Cg Ainul'),
        (BILIK, 'Bilik 3R'),
    )
    rooom = models.CharField(
    max_length=1,
    choices=ROOM_CHOICES,
    default=BILIK,
    )   

    def __str__(self):
        return self.objective


