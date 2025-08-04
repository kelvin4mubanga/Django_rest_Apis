from django.db import models
from django.contrib.auth.models import User


# Coffee shop app models
class CoffeeProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CoffeeOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user}"
