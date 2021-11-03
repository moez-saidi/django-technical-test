from django.contrib import admin

from .models import Comment, Blog


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "blog", "created_at")
    fields = ("text", "blog")

class CommentAdminInline(admin.TabularInline):
    model = Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    fields = ("title", "description",)
