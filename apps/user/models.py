import uuid as uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class User(AbstractUser):
    class Meta:
        ordering = ('-id',)

    avatar = models.ImageField(upload_to='user/images/', null=True, blank=True)
    name = models.CharField(max_length=255)

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.username}"

    @property
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('images/user.png')
