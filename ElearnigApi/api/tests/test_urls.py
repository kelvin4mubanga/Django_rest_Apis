from django.test import TestCase
from django.urls import resolve, reverse
from ..views import CourseList, CourseDetail, EnrollmentList, EnrollmentDetail

class ElearningUrlsTest(TestCase):
    def test_course_list_url_resolves(self):
        url = reverse('course-list')
        self.assertEqual(resolve(url).func.view_class, CourseList)

    def test_course_detail_url_resolves(self):
        url = reverse('course-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, CourseDetail)

    def test_enrollment_list_url_resolves(self):
        url = reverse('enrollment-list')
        self.assertEqual(resolve(url).func.view_class, EnrollmentList)

    def test_enrollment_detail_url_resolves(self):
        url = reverse('enrollment-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, EnrollmentDetail)