from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        db_table = 'Commodity'


