from django.contrib import admin

# Register your models here.
from .models import AuctionCategory, AuctionItem, Bid


admin.site.register(AuctionCategory)
admin.site.register(AuctionItem)
admin.site.register(Bid)