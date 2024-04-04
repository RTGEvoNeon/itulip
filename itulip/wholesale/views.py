import json

#import simplejson as simplejson
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from wholesale.models import *
from wholesale.serializers import * 

# class OrderApiView(generics.ListCreateAPIView):
#     """ Класс обработки GET/POST запросов /orders/ """
#     queryset = Order.objects.all() 
#     serializer_class = OrderSerializer 
#     http_method_names = ['post', 'get']

# class OrderIdApiView(generics.RetrieveUpdateDestroyAPIView):
#     """ Класс обработки GET/PUT/DELETE запросов /orders/id/ """
#     queryset = Order.objects.all()
#     http_method_names = ['get', 'delete', 'put']
#     serializer_class = OrderSerializer

# class ClientApiView(generics.ListCreateAPIView):
#     """ Класс обработки GET/POST запросов /clients/ """
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class ClientIdApiView(generics.RetrieveUpdateDestroyAPIView):
#     """ Класс обработки GET/PUT/DELETE запросов /clients/id/  """
#     queryset = Client.objects.all()
#     http_method_names = ['get', 'delete', 'put']
#     serializer_class = ClientSerializer

# class SortApiView(generics.ListCreateAPIView):
#     """ Класс обработки GET/POST запросов /sorts/ """
#     queryset = Sort.objects.all()
#     serializer_class = SortSerializer

# class SortIdApiView(generics.RetrieveUpdateDestroyAPIView):
#     """ Класс обработки GET/PUT/DELETE запросов /sorts/id/  """
#     queryset = Sort.objects.all()
#     http_method_names = ['get', 'delete', 'put']
#     serializer_class = SortSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с заказами """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes =  (IsAuthenticatedOrReadOnly, )

class SortViewSet(viewsets.ModelViewSet):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer