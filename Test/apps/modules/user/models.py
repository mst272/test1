
from django.db import models

#如果要重写内置注册登入User类的话，要继承AbstractUser
class User(models.Model):
    u_name = models.CharField(max_length=32,unique=True)  #用户名唯一
    u_password = models.CharField(max_length=256)
    bc_id = models.IntegerField()

    class Meta:
        db_table = 'users'

