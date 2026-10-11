from django.urls import path
from .views import (
    CompanyList, CompanyDetail,
    JobCategoryList, JobCategoryDetail,
    JobList, JobDetail,
)

urlpatterns = [
    path('', JobList.as_view(), name='job-list'),
    path('detail/<int:pk>/', JobDetail.as_view(), name='job-detail'),

    path('Company/', CompanyList.as_view(), name='company-list'),
    path('Company/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),

    path('JobCategory/', JobCategoryList.as_view(), name='jobcategory-list'),
    path('JobCategory/<int:pk>/', JobCategoryDetail.as_view(), name='jobcategory-detail'),
]