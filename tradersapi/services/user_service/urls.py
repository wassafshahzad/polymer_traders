from django.urls import path
from .views import UserProfileListCreateAPIView, AuthUserCreateAPIView
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(), name='profile'),
    path('signup/', AuthUserCreateAPIView.as_view(), name='signup'),
]
