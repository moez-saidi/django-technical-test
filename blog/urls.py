from django.urls import path

from .models import Blog
from .views import BlogAPIView, BlogCreateAPIView, CommentCreateAPIView

app_name = "blog"

urlpatterns = [
    path(r"blog/create", BlogCreateAPIView.as_view(), name="create"),
    path(r"blog", BlogAPIView.as_view(queryset=Blog.objects.all()), name=app_name),
    path("comment/create", CommentCreateAPIView.as_view(), name="comment"),
]
