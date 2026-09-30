from django.urls import path
from .views import (
    PollList, PollDetail,
    PollOptionList, PollOptionDetail,
    VoteList, VoteDetail,
)

urlpatterns = [
    path('', PollList.as_view(), name='poll-list'),
    path('<int:pk>/', PollDetail.as_view(), name='poll-detail'),

    path('options/', PollOptionList.as_view(), name='polloption-list'),
    path('options/<int:pk>/', PollOptionDetail.as_view(), name='polloption-detail'),

    path('votes/', VoteList.as_view(), name='vote-list'),
    path('votes/<int:pk>/', VoteDetail.as_view(), name='vote-detail'),
]