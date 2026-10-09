from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from ..models import AuctionCategory, AuctionItem, Bid


class AuctionCategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = AuctionCategory.objects.create(name='Electronics')

    def test_get_category_list(self):
        response = self.client.get('/api/auction/AuctionCategory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        response = self.client.post(
            '/api/auction/AuctionCategory/', {'name': 'Art'}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AuctionCategory.objects.count(), 2)

    def test_get_category_detail(self):
        response = self.client.get(
            f'/api/auction/AuctionCategory/{self.category.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        response = self.client.patch(
            f'/api/auction/AuctionCategory/{self.category.id}/', {'name': 'Gadgets'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete(
            f'/api/auction/AuctionCategory/{self.category.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AuctionItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.seller = User.objects.create_user(username='seller', password='pass123')
        self.category = AuctionCategory.objects.create(name='Electronics')
        self.item = AuctionItem.objects.create(
            title='Vintage Camera',
            description='Rare camera',
            starting_bid=Decimal('100.00'),
            category=self.category,
            seller=self.seller,
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(days=7),
        )

    def test_get_item_list(self):
        response = self.client.get('/api/auction/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Vintage Camera')

    def test_create_item(self):
        self.client.force_authenticate(user=self.seller)
        data = {
            'title': 'Antique Watch',
            'description': 'Old watch',
            'starting_bid': '500.00',
            'category': self.category.id,
            'seller': self.seller.id,
            'start_time': str(timezone.now()),
            'end_time': str(timezone.now() + timedelta(days=5)),
        }
        response = self.client.post('/api/auction/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AuctionItem.objects.count(), 2)

    def test_get_item_detail(self):
        response = self.client.get(f'/api/auction/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        response = self.client.patch(
            f'/api/auction/{self.item.id}/', {'starting_bid': '150.00'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        response = self.client.delete(f'/api/auction/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BidViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.seller = User.objects.create_user(username='seller', password='pass123')
        self.bidder = User.objects.create_user(username='bidder', password='pass123')
        self.item = AuctionItem.objects.create(
            title='Vintage Camera',
            description='Rare',
            starting_bid=Decimal('100.00'),
            seller=self.seller,
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(days=7),
        )
        self.bid = Bid.objects.create(
            auction_item=self.item,
            bidder=self.bidder,
            bid_amount=Decimal('150.00'),
        )

    def test_get_bid_list(self):
        response = self.client.get('/api/auction/Bid/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_bid(self):
        self.client.force_authenticate(user=self.bidder)
        data = {
            'auction_item': self.item.id,
            'bidder': self.bidder.id,
            'bid_amount': '200.00',
        }
        response = self.client.post('/api/auction/Bid/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bid.objects.count(), 2)

    def test_get_bid_detail(self):
        response = self.client.get(f'/api/auction/Bid/{self.bid.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_bid(self):
        response = self.client.delete(f'/api/auction/Bid/{self.bid.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)