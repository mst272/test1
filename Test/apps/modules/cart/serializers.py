from rest_framework import serializers
from .models import Carts

class CartSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    num = serializers.IntegerField()
    class Meta:
        model = Carts
        fields = '__all__'