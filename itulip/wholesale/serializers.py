from rest_framework import serializers

from wholesale.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        many = True
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'phone_number']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        many = True
        fields = ['id', 'full_price', 'prepayment', 'date', 'client']

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        many = True
        fields = '__all__'