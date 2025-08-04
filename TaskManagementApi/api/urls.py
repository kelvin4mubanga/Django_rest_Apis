from django.urls import path
from .views import ProjectList,ProjectDetail,TaskList,TaskDetail,CommentList,CommentDetail




urlpatterns=[
    
   path('<int:pk>/',ProjectDetail.as_view()),
   path('',ProjectList.as_view()),
    
   path('Task/<int:pk>/',TaskDetail.as_view()),
   path('Task/',TaskList.as_view()),
   
   
   path('Comment/<int:pk>/',CommentDetail.as_view()),
   path('Comment/',CommentList.as_view()),



]