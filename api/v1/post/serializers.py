from rest_framework import serializers
from apps.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'title', 'description', 'likes_count']
        read_only_fields = ['author', 'likes_count']

    def to_representation(self, instance):
        return super().to_representation(instance)

    def to_internal_value(self, data):
        request = self.context.get('request')
        if request and request.method in ['PUT', 'PATCH']:
            data = data.copy()
            data.pop('content', None)
        return super().to_internal_value(data)
