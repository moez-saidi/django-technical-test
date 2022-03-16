from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.comment}" by {self.user} at {self.created_on}'

    def save(self, *args, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.user = request.user
        super(Comment, self).save(**kwargs)

    class Meta:
        ordering = ["created_on"]
