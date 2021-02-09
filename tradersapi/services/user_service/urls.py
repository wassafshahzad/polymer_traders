from django.urls import path
from .views import UserProfileListCreateAPIView
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view())
]
