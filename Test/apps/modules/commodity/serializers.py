#序列化器操作
from rest_framework import serializers
from .models import Commodity


class CommoditySerializers(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Commodity
        fields = ('name','price')
