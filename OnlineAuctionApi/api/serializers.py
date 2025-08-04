from rest_framework import serializers
from .models import AuctionCategory, AuctionItem, Bid

class AuctionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionCategory
        fields = '__all__'

class AuctionItemSerializer(serializers.ModelSerializer):
    category = AuctionCategorySerializer(read_only=True)
    seller = serializers.StringRelatedField(read_only=True)
    current_bid = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = AuctionItem
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    auction_item = AuctionItemSerializer(read_only=True)
    bidder = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'
