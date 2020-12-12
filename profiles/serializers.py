from rest_framework import serializers
from .models import Api1,Api2,Review

class Api1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Api1
        exclude = ('id',)

class Api2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Api2
        exclude = ('id',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        exclude =('id','rest_user',)