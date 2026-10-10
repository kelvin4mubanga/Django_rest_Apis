from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (
    PropertyList, PropertyDetail,
    PropertyCategoryList, PropertyCategoryDetail,
    BookingList, BookingDetail,
    ReviewList, ReviewDetail,
)


class PropertyRentalUrlsTest(TestCase):
    def test_property_list_url(self):
        url = reverse('property-list')
        self.assertEqual(resolve(url).func.view_class, PropertyList)

    def test_property_detail_url(self):
        url = reverse('property-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PropertyDetail)

    def test_category_list_url(self):
        url = reverse('category-list')
        self.assertEqual(resolve(url).func.view_class, PropertyCategoryList)

    def test_category_detail_url(self):
        url = reverse('category-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PropertyCategoryDetail)

    def test_booking_list_url(self):
        url = reverse('booking-list')
        self.assertEqual(resolve(url).func.view_class, BookingList)

    def test_booking_detail_url(self):
        url = reverse('booking-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, BookingDetail)

    def test_review_list_url(self):
        url = reverse('review-list')
        self.assertEqual(resolve(url).func.view_class, ReviewList)

    def test_review_detail_url(self):
        url = reverse('review-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ReviewDetail)