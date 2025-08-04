

from rest_framework import generics
from .models import Company, JobCategory, Job
from  .serializers import CompanySerializer,JobCategorySerializer,JobSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class =CompanySerializer



class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Company.objects.all()
    serializer_class = CompanySerializer

class JobCategoryList(generics.ListCreateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class =JobCategorySerializer



class JobCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class =JobSerializer



class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset= Job.objects.all()
    serializer_class = JobSerializer


