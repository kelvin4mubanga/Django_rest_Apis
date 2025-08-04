from django.db import models

# Create your models here.
# Blockchain app models
class BlockchainTransaction(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_hash = models.CharField(max_length=64)

    def __str__(self):
        return self.transaction_hash
