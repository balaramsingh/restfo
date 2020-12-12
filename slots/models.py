from django.db import models
# Create your models here.
from restaurant.models import User

class Slot(models.Model):
    user_name = models.CharField(max_length=100)
    rest_name = models.CharField(max_length=100)
    date = models.DateField()
    slot_number = models.IntegerField()
    table_no = models.IntegerField()

class Table(models.Model):
    user_name = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    tables_2 = models.IntegerField(default=1)
    tables_4 = models.IntegerField(default=1)
    tables_6 = models.IntegerField(default=1)
    tables_8 = models.IntegerField(default=1)
