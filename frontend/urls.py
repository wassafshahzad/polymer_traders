from django.urls import path
from .views import sign_up, welcome_page
urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('', welcome_page, name='welcome')
]
