from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (
    AuctionItemList, AuctionItemDetail,
    AuctionCategoryList, AuctionCategoryDetail,
    BidList, BidDetail,
)


class AuctionUrlsTest(TestCase):
    def test_item_list_url(self):
        url = reverse('auctionitem-list')
        self.assertEqual(resolve(url).func.view_class, AuctionItemList)

    def test_item_detail_url(self):
        url = reverse('auctionitem-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, AuctionItemDetail)

    def test_category_list_url(self):
        url = reverse('auctioncategory-list')
        self.assertEqual(resolve(url).func.view_class, AuctionCategoryList)

    def test_category_detail_url(self):
        url = reverse('auctioncategory-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, AuctionCategoryDetail)

    def test_bid_list_url(self):
        url = reverse('bid-list')
        self.assertEqual(resolve(url).func.view_class, BidList)

    def test_bid_detail_url(self):
        url = reverse('bid-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, BidDetail)