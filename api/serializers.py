from rest_framework import serializers

from api.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'where_from', 'where_to', 'create_date', 'update_date', 'status']


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'status']

