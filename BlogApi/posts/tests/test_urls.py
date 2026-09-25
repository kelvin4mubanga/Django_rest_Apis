from django.test import TestCase
from django.urls import resolve, reverse
from ..views import PostList, PostDetail

class BlogUrlsTest(TestCase):
    def test_post_list_url_resolves(self):
        url = reverse('post-list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail_url_resolves(self):
        url = reverse('post-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetail)