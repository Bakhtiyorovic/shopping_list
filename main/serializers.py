from rest_framework import serializers
from .models import *

class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_item
        fields = '__all__'
        read_only_fields = ['user']