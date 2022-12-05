from django.db import models
from django.contrib.auth. models import User
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    room_num = models.IntegerField()
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)

    def __str__(self) -> str:
        return self.room_num