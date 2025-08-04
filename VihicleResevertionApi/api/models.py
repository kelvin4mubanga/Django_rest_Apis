from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('truck', 'Truck'),
        ('bus', 'Bus'),
        ('bike', 'Bike'),  
    ]
    
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    registration_number = models.CharField(max_length=50, unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.registration_number}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.name} from {self.start_date} to {self.end_date}"
    
    class Meta:
        unique_together = ('vehicle', 'start_date', 'end_date')
