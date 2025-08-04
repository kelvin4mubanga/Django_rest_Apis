from django.urls import path
from .views import PropertyList,PropertyDetail,PropertyCategoryList,PropertyCategoryDetail,BookingList,BookingDetail,ReviewList,ReviewDetail



urlpatterns = [
     path('<int:pk>/',PropertyDetail.as_view()),
    path('', PropertyList.as_view()),
    
     path('PropertyCategory/<int:pk>/',PropertyCategoryDetail.as_view()),
    path('PropertyCategory/',PropertyCategoryList.as_view()),
    
     path('Booking/<int:pk>/',BookingDetail.as_view()),
    path('Booking/',BookingList.as_view()),
    
    
     path('Review/<int:pk>/', ReviewDetail.as_view()),
    path('Review', ReviewList.as_view()),
    
    
    
]
