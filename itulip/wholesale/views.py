import json

#import simplejson as simplejson
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from wholesale.models import *
from wholesale.serializers import * 

class OrderViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с заказами """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с клиентами """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class SortViewSet(viewsets.ModelViewSet):
    """ Вьюсет обработки эндпоинтов, связанных с сортами """
    queryset = Sort.objects.all()
    serializer_class = SortSerializer