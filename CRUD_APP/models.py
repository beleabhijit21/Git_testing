from django.db import models


# Create your models here.
class Order(models.Model):
    oid = models.IntegerField()
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    del_date = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    mail = models.EmailField()
