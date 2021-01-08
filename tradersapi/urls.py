from django.urls import path, include

urlpatterns = [
    path('', include('tradersapi.services.user_service.urls')),
    path('chemical_service/', include('tradersapi.services.chemical_service.urls'))
]
