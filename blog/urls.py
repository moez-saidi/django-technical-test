from django.urls import path
from .views import BlogAPIView, CommentAPIView

app_name = "blog"

urlpatterns = [
    path('comment/', CommentAPIView.as_view(), name = 'comment'),
    path('blog/', BlogAPIView.as_view(), name='blog'),
]
