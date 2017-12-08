from rest_framework import serializers
from .models import Country, City, Seller, Car, Car_brand, Car_model, Car_image
from django.contrib.auth.models import User

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        depth = 1

class CountrySerializer(serializers.ModelSerializer):
    citys = CitySerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        depth = 1

class Car_brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_brand
        fields = '__all__'

class Car_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_model
        fields = '__all__'
        depth = 1

class Car_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_image
        fields = ('id', 'image')

class CarSerializer(serializers.ModelSerializer):
    images = Car_imageSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = '__all__'
        depth = 2