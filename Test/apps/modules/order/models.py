from django.db import models

class Order(models.Model):
    lis = models.ExpressionList
    class Meta:
        db_table = 'Companies'    #定义表的名字
