from django.urls import path
from .views import UserProfileListCreateAPIView, AuthUserCreateAPIView
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view()),
    path('signup/', AuthUserCreateAPIView.as_view())
]
