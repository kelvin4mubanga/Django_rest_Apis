from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (
    MembershipList, MembershipDetail,
    WorkoutSessionList, WorkoutSessionDetail,
)


class GymUrlsTest(TestCase):
    def test_membership_list_url(self):
        url = reverse('membership-list')
        self.assertEqual(resolve(url).func.view_class, MembershipList)

    def test_membership_detail_url(self):
        url = reverse('membership-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, MembershipDetail)

    def test_session_list_url(self):
        url = reverse('session-list')
        self.assertEqual(resolve(url).func.view_class, WorkoutSessionList)

    def test_session_detail_url(self):
        url = reverse('session-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, WorkoutSessionDetail)