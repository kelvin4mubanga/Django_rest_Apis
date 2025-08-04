from django.urls import path
from .views import BlockchainTransactionList,BlockchainTransactionDetail




urlpatterns=[
    
    path('<int:pk>/',BlockchainTransactionDetail.as_view()),
    path('',BlockchainTransactionList.as_view()),

]