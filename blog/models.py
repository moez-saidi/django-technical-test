from django.db import models

class Blog(models.Model):
    """
    Create blog model with corresponding requirements
    """
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=50, blank=False)
    image = models.ImageField(upload_to="blog_image/", blank=False, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Comment blog model with corresponding requirements
    """
    text = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.text


