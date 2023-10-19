from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)