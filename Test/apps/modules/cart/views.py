from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Carts
from .serializers import CartSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#删除
class DeleteView(APIView):
    def post(self, reuqest):
        data = reuqest.data
        de = Carts.objects.filter(name=data['name'])
        de[0].delete()
        return Response({
            'code': 200,
            'message': 'success',
        })

class CartView(APIView):

   #查看购物车
    def get(self,request):
        carts = Carts.objects.all()
        carts_data = CartSerializer(carts,many = True).data   #序列化器,是queryset的时候才需要many==true
        return Response({
            'code': 200,
            'message':'success',
            'data': carts_data
        })

    #添加购物车商品
    def post(self,reuqest):
        data = reuqest.data
        carts = Carts.objects.create(    #添加到数据库里吧
            name=data['name'],
            num=data['num']
        )

        carts_data = CartSerializer(carts).data
        return Response({
            'code': 200,
            'message': 'success',
            'data': carts_data
        })





