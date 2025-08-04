from django.urls import path
from .views import CoffeeProductList,CoffeeOrderDetail




urlpatterns=[
    
    
    path('',CoffeeProductList.as_view()),
    
    path('<int:pk>/',CoffeeProductDetail.as_view()),
    path('order/',CoffeeOrderList.as_view()),
    path('order/<int:pk>/',CoffeeOrderDetail.as_view()),
]