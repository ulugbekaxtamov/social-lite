from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like, Notification


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        if instance.post.author != instance.user:
            try:
                Notification.objects.create(
                    recipient=instance.post.author,
                    post=instance.post,
                    liker=instance.user
                )
            except Exception as e:
                pass
