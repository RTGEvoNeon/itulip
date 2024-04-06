import json

#import simplejson as simplejson
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from wholesale.models import *
from wholesale.serializers import * 
from itulip.wholesale.models import Client

class OrderViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с заказами """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ClientViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ClientViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с клиентами """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientViewSetPagination

class SortViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с сортами """
    queryset = Sort.objects.all()
    serializer_class = SortSerializer