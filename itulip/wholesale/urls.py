from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderList.as_view(), name='ordersView'),
    path('<int:order_id>/', orderView, name='orderView'),
]