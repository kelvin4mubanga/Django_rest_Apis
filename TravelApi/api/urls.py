from django.urls import path
from .views import DestinationList, DestinationDetail,TravelPackageList,TravelPackageDetail,BookingList,BookingDetail,ReviewList,ReviewDetail




urlpatterns=[
    # destination routes
    path('<int:pk>/',DestinationDetail.as_view()),
    path('',DestinationList.as_view()),
    #travel package routes
    path('TravelPackage/<int:pk>/',TravelPackageDetail.as_view()),
    path('TravelPackage/',TravelPackageList.as_view()),
    #booking routes
    path('Booking/<int:pk>/',BookingDetail.as_view()),
    path('Booking/',BookingList.as_view()),
    
    #review routes 
    path('Review/<int:pk>/', ReviewDetail.as_view()),
    path('Review/',ReviewDetail.as_view()),

]