from django.urls import path
from .views import (
    ProjectList, ProjectDetail,
    TaskList, TaskDetail,
    CommentList, CommentDetail,
)

urlpatterns = [
    path('', ProjectList.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project-detail'),

    path('Task/', TaskList.as_view(), name='task-list'),
    path('Task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),

    path('Comment/', CommentList.as_view(), name='comment-list'),
    path('Comment/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]