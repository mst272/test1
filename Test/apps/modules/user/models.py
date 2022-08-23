from django.contrib.auth.models import AbstractUser
from django.db import models

#如果要重写内置注册登入User类的话，要继承AbstractUser
# class User(AbstractUser):
#     #u_name = models.CharField(max_length=32,unique=True)  #用户名唯一
#     #u_password = models.CharField(max_length=256)
#
#     class Meta:
#         db_table = 'Register'

