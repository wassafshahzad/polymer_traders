from django.urls import path, include

urlpatterns = [
    path('user_service/', include('tradersapi.services.user_service.urls')),
    path('chemical_service/', include('tradersapi.services.chemical_service.urls')),
    path('api-auth/', include('dj_rest_auth.urls')),
]
