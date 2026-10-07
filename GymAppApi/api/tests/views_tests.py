from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from ..models import Membership, WorkoutSession


class MembershipViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='member', password='pass123')
        self.membership = Membership.objects.create(
            user=self.user,
            membership_type='Premium',
            start_date=date.today(),
            end_date=date.today() + timedelta(days=365),
        )

    def test_get_membership_list(self):
        response = self.client.get('/api/gym/memberships/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_membership(self):
        new_user = User.objects.create_user(username='newmember', password='pass123')
        data = {
            'user': new_user.id,
            'membership_type': 'Basic',
            'start_date': str(date.today()),
            'end_date': str(date.today() + timedelta(days=30)),
        }
        response = self.client.post('/api/gym/memberships/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Membership.objects.count(), 2)

    def test_get_membership_detail(self):
        response = self.client.get(f'/api/gym/memberships/{self.membership.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['membership_type'], 'Premium')

    def test_update_membership(self):
        response = self.client.patch(
            f'/api/gym/memberships/{self.membership.id}/',
            {'membership_type': 'VIP'},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.membership.refresh_from_db()
        self.assertEqual(self.membership.membership_type, 'VIP')

    def test_delete_membership(self):
        response = self.client.delete(f'/api/gym/memberships/{self.membership.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WorkoutSessionViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='athlete', password='pass123')
        self.session = WorkoutSession.objects.create(
            user=self.user,
            workout_type='Cardio',
            duration=45,
            calories_burned=400,
        )

    def test_get_session_list(self):
        response = self.client.get('/api/gym/sessions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_session(self):
        data = {
            'user': self.user.id,
            'workout_type': 'Strength Training',
            'duration': 60,
            'calories_burned': 500,
        }
        response = self.client.post('/api/gym/sessions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkoutSession.objects.count(), 2)

    def test_get_session_detail(self):
        response = self.client.get(f'/api/gym/sessions/{self.session.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['workout_type'], 'Cardio')

    def test_update_session(self):
        response = self.client.patch(
            f'/api/gym/sessions/{self.session.id}/', {'duration': 50}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_session(self):
        response = self.client.delete(f'/api/gym/sessions/{self.session.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_duration(self):
        response = self.client.post('/api/gym/sessions/', {
            'user': self.user.id,
            'workout_type': 'Yoga',
            'duration': -10,
            'calories_burned': 100,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)