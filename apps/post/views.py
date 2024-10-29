from django.views import generic
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin

from django.db.models import OuterRef, Exists, Count, BooleanField, Value
from .models import Post, Like
from .models import Notification


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 25

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-id').select_related('author').prefetch_related('likes')

        if self.request.user.is_authenticated:
            liked_posts = Like.objects.filter(user=self.request.user, post=OuterRef('pk'))
            queryset = queryset.annotate(
                has_liked=Exists(liked_posts),
                like_count=Count('likes', distinct=True)
            )
        else:
            queryset = queryset.annotate(
                has_liked=Value(False, output_field=BooleanField()),
                like_count=Count('likes', distinct=True)
            )

        return queryset


class MyPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'posts/my_post_list.html'
    context_object_name = 'post_list'
    paginate_by = 25

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by('-id').annotate(like_count=Count('likes', distinct=True))


class NotificationListView(LoginRequiredMixin, generic.ListView):
    model = Notification
    template_name = 'posts/notification_list.html'
    context_object_name = 'notification_list'
    paginate_by = 15

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_count'] = Notification.objects.filter(
            recipient=self.request.user,
            is_read=False
        ).count()
        return context
