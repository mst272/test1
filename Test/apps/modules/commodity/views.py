from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Commodity
from .serializers import CommoditySerializers


class CommodityView(APIView):
    def get(self,request):
        commodity = Commodity.objects.all()
        commodity_data =CommoditySerializers(commodity,many=True).data
        return Response({
            'code': 200,
            'message': 'success',
            'data': commodity_data
        })
