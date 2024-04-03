from rest_framework import serializers

from wholesale.models import *


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        many = True
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'phone_number']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        many = True
        fields = ['id', 'full_price', 'prepayment', 'date', 'client']
