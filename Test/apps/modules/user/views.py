import json
from django.http import JsonResponse, HttpResponse
# django的用户功能库
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
#from .models import User

from django.contrib.auth.models import User

#注册
class Userapiview(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password','')
        email = data.get('email','')

        if username == '' or password == '' or email == '':
            return HttpResponse('不能为空')
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('账号已注册')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse('注册成功！')

#登入
class Login(View):
    def post(self, request):
        # 登录
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')

        # 判断当前用户是否存在,不存在则重新注册
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse('账号未注册')


        # 检测是否为空
        if username == '' or password == '':
            return HttpResponse('不能为空')

        # 验证账号密码正确
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('登入成功')
        else:
            return HttpResponse('密码错误')

#修改密码
class SetPassword(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data.get('username', '')
        old_password = data.get('old_password', '')
        new_password = data.get('new_password', '')

        user = User.objects.get(username=username)

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()   #这一部很重要  没有就不起作用
            return HttpResponse('修改成功')
        else:
            return HttpResponse('密码错误')




