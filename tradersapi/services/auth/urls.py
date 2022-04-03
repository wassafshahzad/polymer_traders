from django.urls import path, include
from .views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('google/', GoogleLogin.as_view(), name='facebook_login'),
]
