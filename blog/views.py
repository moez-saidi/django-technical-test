from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from rest_framework.decorators import action


from rest_framework.response import Response

from blog.models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer


class BlogAPIView(CreateAPIView, ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
