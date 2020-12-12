from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['Restaurant_Name','gmail','Restaurant_Type','Food_Type','contact','Payment_No']

    