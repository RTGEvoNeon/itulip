from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='orders') 
router.register(r'clients', ClientViewSet, basename='clients') 
router.register(r'sorts', SortViewSet, basename='sorts') 

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]