from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Course, Enrollment
from decimal import Decimal

class CourseViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.instructor = User.objects.create_user(
            username='instructor',
            password='instpass123',
            email='instructor@example.com'
        )
        self.student = User.objects.create_user(
            username='student',
            password='studpass123',
            email='student@example.com'
        )
        self.course = Course.objects.create(
            title='Python Programming',
            description='Learn Python from scratch',
            instructor=self.instructor,
            price=99.99
        )
        self.course2 = Course.objects.create(
            title='Django Web Framework',
            description='Build web apps with Django',
            instructor=self.instructor,
            price=149.99
        )

    def test_get_course_list(self):
        response = self.client.get('/api/elearning/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Python Programming')

    def test_create_course_authenticated(self):
        self.client.force_authenticate(user=self.instructor)
        data = {
            'title': 'Data Science with Python',
            'description': 'Learn data analysis and visualization',
            'instructor': self.instructor.id,
            'price': 199.99
        }
        response = self.client.post('/api/elearning/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 3)

    def test_create_course_unauthenticated(self):
        data = {
            'title': 'New Course',
            'description': 'Test',
            'instructor': self.instructor.id,
            'price': 49.99
        }
        response = self.client.post('/api/elearning/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_course_detail(self):
        response = self.client.get(f'/api/elearning/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Learn Python from scratch')

    def test_update_course_authenticated(self):
        self.client.force_authenticate(user=self.instructor)
        data = {'price': 89.99}
        response = self.client.patch(f'/api/elearning/courses/{self.course.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.course.refresh_from_db()
        self.assertEqual(float(self.course.price), 89.99)

    def test_update_course_unauthenticated(self):
        data = {'price': 89.99}
        response = self.client.patch(f'/api/elearning/courses/{self.course.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_course_authenticated(self):
        self.client.force_authenticate(user=self.instructor)
        response = self.client.delete(f'/api/elearning/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 1)

    def test_search_courses(self):
        response = self.client.get('/api/elearning/courses/?search=Python')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python Programming')

    def test_filter_courses_by_price(self):
        response = self.client.get('/api/elearning/courses/?price_lt=100')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python Programming')

class EnrollmentViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = User.objects.create_user(
            username='student',
            password='studpass123'
        )
        self.student2 = User.objects.create_user(
            username='student2',
            password='studpass123'
        )
        self.instructor = User.objects.create_user(
            username='instructor',
            password='instpass123'
        )
        self.course = Course.objects.create(
            title='Python Programming',
            description='Learn Python',
            instructor=self.instructor,
            price=99.99
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course
        )

    def test_get_enrollment_list(self):
        response = self.client.get('/api/elearning/enrollments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_enrollment_authenticated(self):
        self.client.force_authenticate(user=self.student2)
        data = {
            'student': self.student2.id,
            'course': self.course.id
        }
        response = self.client.post('/api/elearning/enrollments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Enrollment.objects.count(), 2)

    def test_create_enrollment_unauthenticated(self):
        data = {
            'student': self.student.id,
            'course': self.course.id
        }
        response = self.client.post('/api/elearning/enrollments/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_enrollment_detail(self):
        response = self.client.get(f'/api/elearning/enrollments/{self.enrollment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['student'], self.student.id)

    def test_delete_enrollment_authenticated(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.delete(f'/api/elearning/enrollments/{self.enrollment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Enrollment.objects.count(), 0)

    def test_prevent_duplicate_enrollment(self):
        self.client.force_authenticate(user=self.student)
        data = {
            'student': self.student.id,
            'course': self.course.id
        }
        response = self.client.post('/api/elearning/enrollments/', data)
        # Should fail due to unique_together constraint
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN])

    def test_get_student_enrollments(self):
        response = self.client.get(f'/api/elearning/enrollments/?student={self.student.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)