from django.urls import path
from .views import NotificationListAPIView, UnreadNotificationListAPIView, NotificationMarkAsReadAPIView

urlpatterns = [
    path('list/', NotificationListAPIView.as_view(), name='notification-list'),
    path('unread/', UnreadNotificationListAPIView.as_view(), name='unread-notification-list'),
    path('<int:id>/read/', NotificationMarkAsReadAPIView.as_view(), name='notification-mark-read'),
]
