from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (
    CompanyList, CompanyDetail,
    JobCategoryList, JobCategoryDetail,
    JobList, JobDetail,
)


class JobListingUrlsTest(TestCase):
    def test_company_list_url(self):
        url = reverse('company-list')
        self.assertEqual(resolve(url).func.view_class, CompanyList)

    def test_company_detail_url(self):
        url = reverse('company-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, CompanyDetail)

    def test_jobcategory_list_url(self):
        url = reverse('jobcategory-list')
        self.assertEqual(resolve(url).func.view_class, JobCategoryList)

    def test_jobcategory_detail_url(self):
        url = reverse('jobcategory-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, JobCategoryDetail)

    def test_job_list_url(self):
        url = reverse('job-list')
        self.assertEqual(resolve(url).func.view_class, JobList)

    def test_job_detail_url(self):
        url = reverse('job-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, JobDetail)