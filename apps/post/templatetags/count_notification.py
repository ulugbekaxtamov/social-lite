from django import template
from apps.post.models import Notification

register = template.Library()


@register.simple_tag
def unread_notifications_count(user):
    try:

        if user.is_authenticated:
            return Notification.objects.filter(recipient=user, is_read=False).count()
        return 0

    except:
        return 0
