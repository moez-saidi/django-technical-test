from rest_framework.test import APITestCase
from model_bakery import baker


class TestBlog(APITestCase):

    def setUp(self):
        baker.make("blog.blog", _quantity=10)
        baker.make("blog.comment", _quantity=10)

    def test_blog(self):
        """
        Add test for blog
        """
        pass
