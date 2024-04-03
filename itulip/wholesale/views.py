import json

#import simplejson as simplejson
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics

from wholesale.models import *
from wholesale.serializers import *


# Методы для ORDERS


# Проверка на тип запроса для /orders/
def ordersView(request):
    if request.method == 'GET':
        return getAllOrders(request)
    elif request.method == 'POST':
        return createOrder(request)


# Проверка на тип запроса для /orders/order_id
def orderView(request, order_id):
    if request.method == 'GET':
        return getOrderById(request, order_id)
    elif request.method == 'PUT':
        return updateOrderById(request, order_id)


# Метод редактирования заказа
def updateOrderById(request, order_id):
    order = Orders.objects.get(pk=order_id)
    data = request.body
    orderParams = OrdersSerializer.update(order, request.body, partial=True)
    return HttpResponse(200)






# Метод получения списка заказов
def getAllOrders(request):
    orders = Orders.objects.all()
    serializer = OrdersSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)


# Метод создания нового заказа
def createOrder(request):
    params = json.loads(request.body)
    client_id = params['client']
    params['client'] = Clients.objects.get(pk=client_id)
    order = Orders(**params)
    order.save()
    return HttpResponse(200)


# Метод получения заказа по id
def getOrderById(request, order_id):
    order = Orders.objects.get(pk=order_id)
    order_json = serializers.serialize('python', [order,])
    return JsonResponse(order_json, safe=False)


# Метод удаления заказа по id
def getOrderById(request, order_id):
    try:
        order = Orders.objects.get(pk=order_id).delete()
        return JsonResponse(status=200)
    except:
        return JsonResponse(status=404)

class OrderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer