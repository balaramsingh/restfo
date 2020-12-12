from django.db import models
from restaurant.models import User
# Create your models here.
class Api1(models.Model):
    restaurant_name = models.CharField(max_length=100)
    date = models.DateField()
    slot_number = models.IntegerField()
    available_2_seater_tables = models.IntegerField()
    available_4_seater_tables = models.IntegerField()
    available_6_seater_tables = models.IntegerField()
    available_8_seater_tables = models.IntegerField()

class Api2(models.Model):
    restaurant_name = models.CharField(max_length=100)
    date = models.DateField()
    table_size = models.IntegerField()
    slot_1_status = models.CharField(max_length=20)
    slot_2_status = models.CharField(max_length=20)
    slot_3_status = models.CharField(max_length=20)
    slot_4_status = models.CharField(max_length=20)
    slot_5_status = models.CharField(max_length=20)
    slot_6_status = models.CharField(max_length=20)
    slot_7_status = models.CharField(max_length=20)
    slot_8_status = models.CharField(max_length=20)
    slot_9_status = models.CharField(max_length=20)
    slot_10_status = models.CharField(max_length=20)
    slot_11_status = models.CharField(max_length=20)
    slot_12_status = models.CharField(max_length=20)
    slot_13_status = models.CharField(max_length=20)
    slot_14_status = models.CharField(max_length=20)
    slot_15_status = models.CharField(max_length=20)
    slot_16_status = models.CharField(max_length=20)
    slot_17_status = models.CharField(max_length=20)
    slot_18_status = models.CharField(max_length=20)
    slot_19_status = models.CharField(max_length=20)
    slot_20_status = models.CharField(max_length=20)


class Review(models.Model):
    rest_name = models.CharField(max_length=256,null=True)
    rest_user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=30,null=True)
    experience = models.CharField(max_length=20,null=True)
    rating = models.IntegerField(null=True)
