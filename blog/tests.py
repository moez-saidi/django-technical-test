from django.core.files.images import ImageFile

from rest_framework.test import APITestCase
from unittest.mock import MagicMock

from model_bakery import baker

from rest_framework.test import APIClient

from .models import Blog, Comment


class TestBlog(APITestCase):

    def setUp(self):
        baker.make("blog.blog", _quantity=10)
        baker.make("blog.comment", _quantity=10)
        client = APIClient()

        self.image = MagicMock(spec=ImageFile, name="FileMock")
        self.image.name = "img.jpg"
        
    def test_blog(self):
        """
        Add test for blog
        """
        blogs = Blog.objects.count()
        comments = Comment.objects.count()
        assert blogs == comments

    def test_create_blog_without_title(self):
        response = self.client.post('/api/blog/', {'title': "", "description": "test description"}, files=dict(image=self.image), format='json')
        assert response.status_code == 400 
        assert response.json() == {'title': ['This field may not be blank.']}
        

    def test_create_blog(self):
        blog_data = {
            'title': "My test title",
            "description": "test description"
        }

        blog_response = self.client.post('/api/blog/', blog_data)
        
        assert blog_response.status_code == 201
        assert blog_data['title'] == blog_response.json()["title"] 


    def test_list_comments_by_blog(self):

        comment_data = {
            'text': 'my comment',
            'blog': 1 # blog created previously
        }
        
        comment_response = self.client.post('/api/comment/', comment_data)

        assert comment_response.status_code == 201
        assert comment_data['text'] == comment_response.json()["text"]
