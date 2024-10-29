from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.post.models import Notification
from .serializers import NotificationSerializer


class NotificationListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


class UnreadNotificationListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, is_read=False)


class NotificationMarkAsReadAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"detail": "Not authorized."}, status=status.HTTP_403_FORBIDDEN)

        notification.is_read = True
        notification.save(update_fields=['is_read'])
        return Response({"detail": "Notification marked as read.", "is_read": True}, status=status.HTTP_200_OK)
