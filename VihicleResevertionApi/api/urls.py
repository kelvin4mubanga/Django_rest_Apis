from django.urls import path
from .views import VehicleListView,VehicleDetailsView,ReservationListView,ReservationDetailsView




urlpatterns=[
    
    path('<int:pk>/',VehicleDetailsView.as_view()),
    path('',VehicleListView.as_view()),
    
     path('Reservation/<int:pk>/',ReservationDetailsView.as_view()),
    path('Reservation/',ReservationListView.as_view()),

]