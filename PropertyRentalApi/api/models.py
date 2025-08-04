
from django.db import models
from django.contrib.auth.models import User

class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    category = models.ForeignKey(PropertyCategory, related_name='properties', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    available_from = models.DateField()
    available_to = models.DateField()
    image = models.ImageField(upload_to='properties/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    property = models.ForeignKey(Property, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.property.title}"

class Review(models.Model):
    property = models.ForeignKey(Property, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review of {self.property.title} by {self.user.username}"
