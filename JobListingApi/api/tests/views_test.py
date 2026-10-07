from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from ..models import Company, JobCategory, Job


class CompanyViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(
            name='TechCorp',
            location='San Francisco',
            website='https://techcorp.com',
            description='A tech company',
        )

    def test_get_company_list(self):
        response = self.client.get('/api/jobs/Company/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_company(self):
        data = {
            'name': 'DataInc',
            'location': 'NYC',
            'website': 'https://datainc.com',
            'description': 'Data analytics company',
        }
        response = self.client.post('/api/jobs/Company/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)

    def test_get_company_detail(self):
        response = self.client.get(f'/api/jobs/Company/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        response = self.client.patch(
            f'/api/jobs/Company/{self.company.id}/', {'location': 'Remote'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_company(self):
        response = self.client.delete(f'/api/jobs/Company/{self.company.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class JobCategoryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = JobCategory.objects.create(name='Engineering')

    def test_get_category_list(self):
        response = self.client.get('/api/jobs/JobCategory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        response = self.client.post('/api/jobs/JobCategory/', {'name': 'Design'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category_detail(self):
        response = self.client.get(
            f'/api/jobs/JobCategory/{self.category.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete(
            f'/api/jobs/JobCategory/{self.category.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class JobViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(
            name='TechCorp', location='SF', description='Tech'
        )
        self.category = JobCategory.objects.create(name='Engineering')
        self.job = Job.objects.create(
            title='Backend Developer',
            company=self.company,
            category=self.category,
            job_type='full_time',
            description='Build APIs',
            location='Remote',
            salary_range='$80k - $120k',
            last_date_to_apply=date.today() + timedelta(days=30),
        )

    def test_get_job_list(self):
        response = self.client.get('/api/jobs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Backend Developer')

    def test_create_job(self):
        data = {
            'title': 'Frontend Developer',
            'company': self.company.id,
            'category': self.category.id,
            'job_type': 'contract',
            'description': 'Build UIs',
            'location': 'NYC',
            'salary_range': '$70k - $100k',
            'last_date_to_apply': str(date.today() + timedelta(days=20)),
        }
        response = self.client.post('/api/jobs/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 2)

    def test_get_job_detail(self):
        response = self.client.get(f'/api/jobs/detail/{self.job.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_job(self):
        response = self.client.patch(
            f'/api/jobs/detail/{self.job.id}/', {'salary_range': '$90k - $130k'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_job(self):
        response = self.client.delete(f'/api/jobs/detail/{self.job.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_jobs_by_type(self):
        response = self.client.get('/api/jobs/?job_type=full_time')
        self.assertEqual(response.status_code, status.HTTP_200_OK)