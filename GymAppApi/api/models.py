from django.db import models

# Create your models here.
from django.contrib.auth.models import User






# Gym app models
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Membership for {self.user}"

class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()

    def __str__(self):
        return f"Session by {self.user}"
