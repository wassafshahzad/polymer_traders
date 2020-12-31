from django.urls import path, include

urlpatterns = [
    path('', include('tradersapi.services.user_service.urls')),
]
