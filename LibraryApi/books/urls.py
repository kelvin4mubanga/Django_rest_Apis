from django.urls import path
from .views import BookListView,BookDetailsView




urlpatterns=[
    
    path('<int:pk>/',BookDetailsView.as_view()),
    path('',BookListView.as_view()),

]