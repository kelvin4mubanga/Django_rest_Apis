from rest_framework import serializers
from .models import Company, JobCategory, Job

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    category = JobCategorySerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
