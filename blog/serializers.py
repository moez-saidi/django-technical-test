from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Blog, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def save(self, **kwargs):
        self.user = UserSerializer(kwargs.pop("user"), read_only=True)

    class Meta:
        model = Comment
        fields = ("comment", "created_on", "user", "blog")


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = ("title", "description", "image", "comments")
