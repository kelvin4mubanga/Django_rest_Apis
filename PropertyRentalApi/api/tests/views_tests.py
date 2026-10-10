from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from decimal import Decimal
from ..models import PropertyCategory, Property, Booking, Review


class PropertyCategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = PropertyCategory.objects.create(name='Apartment')

    def test_get_category_list(self):
        response = self.client.get('/api/property/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_category(self):
        response = self.client.post('/api/property/categories/', {'name': 'Villa'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PropertyCategory.objects.count(), 2)

    def test_get_category_detail(self):
        response = self.client.get(f'/api/property/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        response = self.client.patch(
            f'/api/property/categories/{self.category.id}/', {'name': 'Condo'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Condo')

    def test_delete_category(self):
        response = self.client.delete(f'/api/property/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PropertyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='pass123')
        self.category = PropertyCategory.objects.create(name='Apartment')
        self.property = Property.objects.create(
            title='Beach House',
            description='Nice beach house',
            price_per_night=Decimal('150.00'),
            location='Miami',
            category=self.category,
            owner=self.owner,
            available_from=date.today(),
            available_to=date.today() + timedelta(days=30),
        )

    def test_get_property_list(self):
        response = self.client.get('/api/property/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Beach House')

    def test_create_property(self):
        self.client.force_authenticate(user=self.owner)
        data = {
            'title': 'City Loft',
            'description': 'Downtown loft',
            'price_per_night': '200.00',
            'location': 'NYC',
            'category': self.category.id,
            'owner': self.owner.id,
            'available_from': str(date.today()),
            'available_to': str(date.today() + timedelta(days=15)),
        }
        response = self.client.post('/api/property/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 2)

    def test_get_property_detail(self):
        response = self.client.get(f'/api/property/{self.property.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_property(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(
            f'/api/property/{self.property.id}/', {'price_per_night': '175.00'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.property.refresh_from_db()
        self.assertEqual(self.property.price_per_night, Decimal('175.00'))

    def test_delete_property(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(f'/api/property/{self.property.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_nonexistent_property(self):
        response = self.client.get('/api/property/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='pass123')
        self.guest = User.objects.create_user(username='guest', password='pass123')
        self.property = Property.objects.create(
            title='Beach House',
            description='Nice',
            price_per_night=Decimal('150.00'),
            location='Miami',
            owner=self.owner,
            available_from=date.today(),
            available_to=date.today() + timedelta(days=30),
        )
        self.booking = Booking.objects.create(
            property=self.property,
            user=self.guest,
            check_in=date.today() + timedelta(days=1),
            check_out=date.today() + timedelta(days=3),
            total_price=Decimal('300.00'),
        )

    def test_get_booking_list(self):
        response = self.client.get('/api/property/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        self.client.force_authenticate(user=self.guest)
        data = {
            'property': self.property.id,
            'user': self.guest.id,
            'check_in': str(date.today() + timedelta(days=5)),
            'check_out': str(date.today() + timedelta(days=7)),
            'total_price': '300.00',
        }
        response = self.client.post('/api/property/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_get_booking_detail(self):
        response = self.client.get(f'/api/property/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_booking(self):
        response = self.client.delete(f'/api/property/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ReviewViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='pass123')
        self.reviewer = User.objects.create_user(username='reviewer', password='pass123')
        self.property = Property.objects.create(
            title='Beach House',
            description='Nice',
            price_per_night=Decimal('150.00'),
            location='Miami',
            owner=self.owner,
            available_from=date.today(),
            available_to=date.today() + timedelta(days=30),
        )
        self.review = Review.objects.create(
            property=self.property,
            user=self.reviewer,
            rating=5,
            comment='Amazing stay!',
        )

    def test_get_review_list(self):
        response = self.client.get('/api/property/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        self.client.force_authenticate(user=self.reviewer)
        data = {
            'property': self.property.id,
            'user': self.reviewer.id,
            'rating': 4,
            'comment': 'Good place',
        }
        response = self.client.post('/api/property/reviews/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_review_detail(self):
        response = self.client.get(f'/api/property/reviews/{self.review.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_review(self):
        response = self.client.patch(
            f'/api/property/reviews/{self.review.id}/', {'rating': 3}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_review(self):
        response = self.client.delete(f'/api/property/reviews/{self.review.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)