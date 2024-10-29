from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),

    path('post/', include('api.v1.post.urls')),

    path('notification/', include('api.v1.notification.urls')),

]
