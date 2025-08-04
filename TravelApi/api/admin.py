from django.contrib import admin
from .models import Destination, TravelPackage, Booking, Review
# Register your models here.
admin.site.register(Destination)
admin.site.register(TravelPackage)
admin.site.register(Booking)
admin.site.register(Review)