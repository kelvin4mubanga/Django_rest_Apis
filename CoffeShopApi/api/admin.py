from django.contrib import admin
from .models import CoffeeProduct,CoffeeOrder
# Register your models here.


admin.site.register(CoffeeProduct)
admin.site.register(CoffeeOrder)