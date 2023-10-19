from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    date = models.DateField()
    email = models.EmailField()
    repeat_email = models.EmailField()
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)