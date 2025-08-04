from django.contrib import admin

# Register your models here.
from .models import Vehicle,Reservation
admin.site.register(Vehicle)
admin.site.register(Reservation)