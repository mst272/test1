from django.db import models


class Carts(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()

    class Meta:
        db_table = 'Cart'

