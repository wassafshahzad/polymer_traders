from django.urls import path
from .views import UserProfileListCreateAPIView, AuthUserCreateAPIView, CreateListUserProduct, \
    UserProductRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('profiles/', UserProfileListCreateAPIView.as_view(), name='profile'),
    path('signup/', AuthUserCreateAPIView.as_view(), name='signup'),
    path('profiles/products/',
         CreateListUserProduct.as_view(), name='get_product'),
    path('profiles/products/<int:pk>/',
         UserProductRetrieveUpdateDestroyAPIView.as_view(), name='get_single_product'),

]
