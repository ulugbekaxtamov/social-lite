from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from api.v1.user.serializers import UserSerializer
from api.v1.user.swagger_docs import profile_update_docs
from apps.user.models import User


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user

    @profile_update_docs()
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @profile_update_docs()
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
