from rest_framework import serializers
from .models import Menu
class MenuSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['fname','price','category','veg','availability','rating','no_of_rated']
