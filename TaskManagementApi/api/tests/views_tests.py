from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from ..models import Project, Task, Comment


class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='pass123')
        self.project = Project.objects.create(
            name='Website Redesign',
            description='Redesign company website',
            owner=self.owner,
        )

    def test_get_project_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Website Redesign')

    def test_create_project(self):
        self.client.force_authenticate(user=self.owner)
        data = {
            'name': 'Mobile App',
            'description': 'Build mobile app',
            'owner': self.owner.id,
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)

    def test_get_project_detail(self):
        response = self.client.get(f'/api/tasks/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        response = self.client.patch(
            f'/api/tasks/{self.project.id}/', {'name': 'Website Redesign v2'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, 'Website Redesign v2')

    def test_delete_project(self):
        response = self.client.delete(f'/api/tasks/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='pass123')
        self.assignee = User.objects.create_user(username='assignee', password='pass123')
        self.project = Project.objects.create(
            name='Website', description='Desc', owner=self.owner
        )
        self.task = Task.objects.create(
            project=self.project,
            title='Design homepage',
            description='Create mockups',
            assignee=self.assignee,
            status='todo',
            priority=2,
            due_date=date.today() + timedelta(days=7),
        )

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/Task/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {
            'project': self.project.id,
            'title': 'Build login page',
            'description': 'Implement login',
            'assignee': self.assignee.id,
            'status': 'todo',
            'priority': 3,
            'due_date': str(date.today() + timedelta(days=10)),
        }
        response = self.client.post('/api/tasks/Task/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_detail(self):
        response = self.client.get(f'/api/tasks/Task/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task_status(self):
        response = self.client.patch(
            f'/api/tasks/Task/{self.task.id}/', {'status': 'in_progress'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'in_progress')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/Task/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_tasks_by_status(self):
        Task.objects.create(
            project=self.project, title='Task 2', status='completed', priority=1
        )
        response = self.client.get('/api/tasks/Task/?status=completed')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CommentViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.project = Project.objects.create(
            name='P1', description='D', owner=self.user
        )
        self.task = Task.objects.create(project=self.project, title='T1')
        self.comment = Comment.objects.create(
            task=self.task, user=self.user, text='Looks good!'
        )

    def test_get_comment_list(self):
        response = self.client.get('/api/tasks/Comment/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        data = {
            'task': self.task.id,
            'user': self.user.id,
            'text': 'Please update the design',
        }
        response = self.client.post('/api/tasks/Comment/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comment_detail(self):
        response = self.client.get(f'/api/tasks/Comment/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        response = self.client.patch(
            f'/api/tasks/Comment/{self.comment.id}/', {'text': 'Updated'}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        response = self.client.delete(f'/api/tasks/Comment/{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)