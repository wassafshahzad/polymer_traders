from django.urls import path
from .views import UserProfileListCreateAPIView, AuthUserCreateAPIView, UserPostListCreateAPIView
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(), name='profile'),
    path('signup/', AuthUserCreateAPIView.as_view(), name='signup'),
    path('posts/', UserPostListCreateAPIView.as_view(), name='posts')
]
