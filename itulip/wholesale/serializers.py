from rest_framework import serializers

from wholesale.models import *


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Client
        many = True
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        many = True
        fields = '__all__'
        

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        many = True
        fields = '__all__'