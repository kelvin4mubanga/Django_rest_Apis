
from django.urls import path
from .views import CompanyList,CompanyDetail,JobCategoryList,JobCategoryDetail,JobList,JobDetail

urlpatterns = [
    
    
   path('',JobList.as_view()),
   path('detail/<int:pk>/',JobDetail.as_view()),
   
   
   path('Company/',CompanyList.as_view()),
   path('Company/<int:pk>/', CompanyDetail.as_view()),
   
   path('JobCategory/',JobCategoryList.as_view()),
   path('JobCategory/<int:pk>/',JobCategoryDetail.as_view()),
   
]
