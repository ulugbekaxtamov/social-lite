from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('list/', views.PostListView.as_view(), name='post_list'),
    path('my-posts/', views.MyPostListView.as_view(), name='my_post_list'),
    path('notifications/', views.NotificationListView.as_view(), name='notification_list'),
]
