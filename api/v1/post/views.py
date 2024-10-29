from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter

from apps.post.models import Post, Like
from .serializers import PostSerializer
from .swagger_docs import post_create_docs, post_like_toggle_docs


class PostListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]

    @post_create_docs()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied("You do not have permission to update this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        instance.delete()


class PostLikedListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        liked_posts = Post.objects.filter(likes__user=self.request.user)
        return liked_posts


class PostLikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @post_like_toggle_docs()
    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs.exists():
            like_qs.delete()
            liked = False
        else:
            Like.objects.create(user=request.user, post=post)
            liked = True

        return Response({
            "liked": liked,
            "likes_count": post.likes.count()
        }, status=status.HTTP_200_OK)


class UserPostListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
