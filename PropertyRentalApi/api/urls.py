from django.urls import path
from .views import (
    PropertyList, PropertyDetail,
    PropertyCategoryList, PropertyCategoryDetail,
    BookingList, BookingDetail,
    ReviewList, ReviewDetail,
)

urlpatterns = [
    path('', PropertyList.as_view(), name='property-list'),
    path('<int:pk>/', PropertyDetail.as_view(), name='property-detail'),

    path('categories/', PropertyCategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', PropertyCategoryDetail.as_view(), name='category-detail'),

    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),

    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]