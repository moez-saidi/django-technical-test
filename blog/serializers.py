from rest_framework import serializers

from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Create comment serializer
    """

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("created_at",)


class BlogSerializer(serializers.ModelSerializer):
    """
    Create blog serializer
    """

    class Meta:
        model = Blog
        fields = "__all__"
