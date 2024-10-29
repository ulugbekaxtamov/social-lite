from rest_framework import serializers
from apps.post.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'post', 'liker', 'is_read', 'created_at']
        read_only_fields = ['id', 'recipient', 'post', 'liker', 'created_at']
