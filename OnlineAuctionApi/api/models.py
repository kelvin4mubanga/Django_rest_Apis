
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class AuctionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AuctionItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(AuctionCategory, related_name='items', on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, related_name='auction_items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='auction_items/', null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Bid(models.Model):
    auction_item = models.ForeignKey(AuctionItem, related_name='bids', on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, related_name='bids', on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid of {self.bid_amount} on {self.auction_item.title} by {self.bidder.username}"
