from django.db import models

from apps.base.models import Base
from apps.user.models import User


class Post(Base):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.FileField(upload_to='posts/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.id} - {self.author}"

    @property
    def likes_count(self):
        return self.likes.count()


class Like(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        ordering = ['-id']
        constraints = [models.UniqueConstraint(fields=['user', 'post'], name='unique_user_post_like')]

    def __str__(self):
        return f"{self.id} {self.user.name} {self.post}"


class Notification(Base):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_notifications')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.recipient} - {self.liker}"

    class Meta:
        ordering = ['is_read', '-created_at']
