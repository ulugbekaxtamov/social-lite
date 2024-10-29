import django_filters
from django.db.models import Count
from apps.post.models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', field_name='title')
    likes = django_filters.ChoiceFilter(
        method='filter_by_likes_count',
        choices=[('high', 'High'), ('low', 'Low')],
        label="Likes count"
    )

    class Meta:
        model = Post
        fields = ['title', 'likes']

    def filter_by_likes_count(self, queryset, name, value):
        queryset = queryset.annotate(total_likes=Count('likes'))

        if value == 'high':
            return queryset.filter(total_likes__gt=10)
        elif value == 'low':
            return queryset.filter(total_likes__lte=10)

        return queryset
