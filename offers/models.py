from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    restname = models.CharField(max_length=20)
    title = models.CharField(max_length=20, default="Mega Discount")
    code = models.CharField(max_length=50)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],null=True)
    applicable = models.CharField(max_length=100, default="ALL USERS")
    description = models.CharField(max_length=100, default="If Applicable -> Please Redeem This Coupon When You Vist Our Restaurant.!!")
