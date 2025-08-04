from django.contrib import admin
from .models import Property, PropertyCategory,Booking,Review
# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyCategory)
admin.site.register(Booking)
admin.site.register(Review)