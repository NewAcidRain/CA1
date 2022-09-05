from rest_framework import serializers
from Cigarettes.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelProduct
        fields = ('id', 'name', 'brand', 'price')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelProduct
        fields = ('brand',)


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField(required=False)
    chat_id = serializers.IntegerField(required=False)

    class Meta:
        model = ModelCart
        fields = ('product', 'quantity', 'chat_id')

    @staticmethod
    def delete(instance, validation_data):
        instance.product = validation_data.get('product')
        instance.quantity = validation_data.get('quantity')
        instance.chat_id = validation_data.get('chat_id')
        instance.save()
        return instance
