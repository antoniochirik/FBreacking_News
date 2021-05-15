from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserProfileListCreateView


urlpatterns = [
    path('',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('users',
         UserProfileListCreateView.as_view(),
         name='all_profiles')
]
