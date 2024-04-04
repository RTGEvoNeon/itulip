from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet, basename='orders') 

urlpatterns = [
    path('', include(router.urls)),
    # path('orders/', OrderApiView.as_view()),
    # path('orders/<int:pk>/', OrderIdApiView.as_view()),
    # path('clients/', ClientApiView.as_view()),
    # path('clients/<int:pk>/', ClientIdApiView.as_view()),
    # path('sorts/', SortApiView.as_view()),
    # path('sorts/<int:pk>/', SortIdApiView.as_view()),

]