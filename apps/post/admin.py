from django.contrib import admin
from .models import Post, Like, Notification


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'description', 'likes_count', 'created_at', 'updated_at', 'is_delete')
    search_fields = ('title', 'description', 'author__username', 'author__email')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('likes_count',)
    date_hierarchy = 'created_at'

    def likes_count(self, obj):
        return obj.likes_count

    likes_count.short_description = 'Likes Count'

    def get_queryset(self, request):
        return Post.all_objects.all()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at', 'updated_at', 'is_delete')
    search_fields = ('user__username', 'user__email', 'post__title')
    list_filter = ('created_at', 'updated_at', 'is_delete')
    date_hierarchy = 'created_at'

    def get_queryset(self, request):
        return Like.all_objects.all()


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'post', 'liker', 'is_read', 'created_at', 'updated_at', 'is_delete')
    search_fields = ('recipient__username', 'recipient__email', 'liker__username', 'liker__email', 'post__title')
    list_filter = ('is_read', 'created_at', 'updated_at', 'is_delete')
    date_hierarchy = 'created_at'
    list_editable = ('is_read',)

    def get_queryset(self, request):
        return Notification.all_objects.all()
