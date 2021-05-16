from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import User
from .permissions import IsStaffOrCreateOnly
from .serializers import UserSerializer


class UserProfileListCreateView(ListCreateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffOrCreateOnly, ]
    pagination_class = PageNumberPagination
