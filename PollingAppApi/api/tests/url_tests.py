from django.test import TestCase
from django.urls import resolve, reverse
from ..views import (
    PollList, PollDetail,
    PollOptionList, PollOptionDetail,
    VoteList, VoteDetail,
)


class PollingUrlsTest(TestCase):
    def test_poll_list_url(self):
        url = reverse('poll-list')
        self.assertEqual(resolve(url).func.view_class, PollList)

    def test_poll_detail_url(self):
        url = reverse('poll-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PollDetail)

    def test_polloption_list_url(self):
        url = reverse('polloption-list')
        self.assertEqual(resolve(url).func.view_class, PollOptionList)

    def test_polloption_detail_url(self):
        url = reverse('polloption-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PollOptionDetail)

    def test_vote_list_url(self):
        url = reverse('vote-list')
        self.assertEqual(resolve(url).func.view_class, VoteList)

    def test_vote_detail_url(self):
        url = reverse('vote-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, VoteDetail)