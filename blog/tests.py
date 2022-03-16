from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from model_bakery.recipe import Recipe
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Blog, Comment


class BlogTest(APITestCase):
    def setUp(self):
        self.blogs = baker.make("blog.blog", _quantity=10)
        self.blog_url = reverse("blog:blog")

    def test_blog(self):
        """
        Add test for blog.
        """
        response = self.client.get(self.blog_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Blog.objects.count(), 10)


class CreateBlogTest(APITestCase):
    def setUp(self):
        self.blog_url = reverse("blog:create")

    def test_create_blog(self):
        data = {"title": "blog", "description": "blog description"}
        response = self.client.post(self.blog_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            {
                "title": "blog",
                "description": "blog description",
                "image": None,
                "comments": [],
            },
        )


class CreateCommentTest(APITestCase):
    def setUp(self):
        self.blog = baker.make("blog.blog")
        self.blog_url = reverse("blog:blog")
        self.url = reverse("blog:comment")
        self.user = User.objects.create(username="sean")

    def test_create_comment(self):
        data = {"comment": "this is a comment", "blog": 1, "user": 2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        comment1 = Recipe(Comment, blog=self.blog)
        comment1.make(comment="this is a comment")

        comment2 = Recipe(Comment, blog=self.blog)
        comment2.make(comment="this is another comment")

        self.assertEquals(self.blog.comments.count(), 2)
