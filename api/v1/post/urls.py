from django.urls import path
from .views import (
    PostListAPIView, PostCreateAPIView, PostDetailAPIView,
    PostLikeToggleAPIView, PostLikedListAPIView, UserPostListAPIView
)

app_name = 'api_post'

urlpatterns = [
    # POST
    path('list/', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='retrieve_update_destroy'),

    path('my/', UserPostListAPIView.as_view(), name='user-post-list'),

    path('liked/', PostLikedListAPIView.as_view(), name='user_liked_posts'),
    path('<int:pk>/like/', PostLikeToggleAPIView.as_view(), name='post-like-toggle'),

]
