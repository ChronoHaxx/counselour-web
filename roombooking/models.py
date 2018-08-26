from django.db import models

# Create your models here.
class booking(models.Model):
    ROOM_CHOICES =  (
                ('TF', 'Teacher Fazilawati'),
                ('TA', 'Teacher Ar'),
                ('RR', '3R room'),
        )
    room = models.CharField(max_length=2, choices=ROOM_CHOICES)
    date = models.DateTimeField()
    duration = models.DurationField()
    objective = models.TextField()
    #user = models.ForeignKey()

    def __str__(self):
        return (self.room)
