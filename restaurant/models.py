from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
import requests,geocoder

g = geocoder.ip('me')
lat= g.lat
lng=g.lng
Authorization="9828a5olhddjq4o3mozc7dvw1bevgwwo"
base_url="http://apis.mapmyindia.com/advancedmaps/v1/"+Authorization+"/rev_geocode?lat="+str(lat)+"&lng="+str(lng)
val=requests.get(base_url)
val=val.json()
country=val['results'][0]['area']
state=val['results'][0]['state']
district=val['results'][0]['district']
sub_zone=val['results'][0]['subDistrict']

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = PhoneNumberField(blank=True)
    gmail = models.CharField(max_length=500,blank=True)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Restaurant_Name=models.CharField(max_length=100)
    gmail = models.CharField(max_length=50,null=True)
    lat = models.FloatField(default=lat)
    lon = models.FloatField(default=lng)
    Address=models.CharField(max_length=500)
    Restaurant_Type=models.CharField(max_length=50)
    Food_Type=models.CharField(max_length=50)
    Restaurant_Image = models.ImageField(default='rest_logo/default.jpg', upload_to='rest_logo')
    Country=models.CharField(max_length=50,default=country)
    State=models.CharField(max_length=50,default=state)
    district=models.CharField(max_length=50,default=district)
    sub_zone=models.CharField(max_length=50,default=sub_zone)
    contact = PhoneNumberField(blank=True)
    Payment_No = PhoneNumberField(blank=True)
