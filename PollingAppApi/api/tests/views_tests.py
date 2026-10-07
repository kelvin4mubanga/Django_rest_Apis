from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Poll, PollOption, Vote


class PollViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.poll = Poll.objects.create(
            question='Best programming language?',
            created_by=self.user,
        )

    def test_get_poll_list(self):
        response = self.client.get('/api/polls/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], 'Best programming language?')

    def test_create_poll(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'question': 'Favourite framework?',
            'created_by': self.user.id,
        }
        response = self.client.post('/api/polls/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Poll.objects.count(), 2)

    def test_get_poll_detail(self):
        response = self.client.get(f'/api/polls/{self.poll.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_poll(self):
        response = self.client.patch(
            f'/api/polls/{self.poll.id}/', {'question': 'Updated question?'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.poll.refresh_from_db()
        self.assertEqual(self.poll.question, 'Updated question?')

    def test_delete_poll(self):
        response = self.client.delete(f'/api/polls/{self.poll.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_nonexistent_poll(self):
        response = self.client.get('/api/polls/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PollOptionViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.poll = Poll.objects.create(question='Q?', created_by=self.user)
        self.option = PollOption.objects.create(poll=self.poll, option_text='Python')

    def test_get_option_list(self):
        response = self.client.get('/api/polls/options/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_option(self):
        data = {'poll': self.poll.id, 'option_text': 'JavaScript'}
        response = self.client.post('/api/polls/options/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PollOption.objects.count(), 2)

    def test_get_option_detail(self):
        response = self.client.get(f'/api/polls/options/{self.option.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_option(self):
        response = self.client.patch(
            f'/api/polls/options/{self.option.id}/', {'option_text': 'Python 3'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_option(self):
        response = self.client.delete(f'/api/polls/options/{self.option.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class VoteViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.poll = Poll.objects.create(question='Q?', created_by=self.user)
        self.option = PollOption.objects.create(poll=self.poll, option_text='Python')
        self.vote = Vote.objects.create(
            poll=self.poll, option=self.option, user=self.user
        )

    def test_get_vote_list(self):
        response = self.client.get('/api/polls/votes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vote(self):
        new_user = User.objects.create_user(username='user2', password='pass123')
        data = {
            'poll': self.poll.id,
            'option': self.option.id,
            'user': new_user.id,
        }
        response = self.client.post('/api/polls/votes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 2)

    def test_get_vote_detail(self):
        response = self.client.get(f'/api/polls/votes/{self.vote.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vote(self):
        response = self.client.delete(f'/api/polls/votes/{self.vote.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)