


from django.urls import path
from .views import AuctionItemList,AuctionItemDetail,AuctionCategoryList,AuctionCategoryDetail,BidList,BidDetail



urlpatterns = [
     path('<int:pk>/',AuctionItemDetail.as_view()),
    path('', AuctionItemList.as_view()),
    
     path('AuctionCategory/<int:pk>/',AuctionCategoryDetail.as_view()),
    path('AuctionCategory/',AuctionCategoryList.as_view()),
    
     path('Bid/<int:pk>/',BidDetail.as_view()),
    path('Bid/',BidList.as_view()),
    
    
     #path('Review/<int:pk>/', ReviewDetail.as_view()),
    #path('Review', ReviewList.as_view()),
    
    
    
]
