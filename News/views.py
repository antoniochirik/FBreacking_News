from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination


from .permissions import IsStaffOrReadOnly
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    ordering_fields = ['pub_date',]
    search_fields = ['text', 'head']
    permission_classes = [IsStaffOrReadOnly, permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
