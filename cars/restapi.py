from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Country, City, Seller, Car_brand, Car_model, Car_image, Car
from .serializers import CountrySerializer, CitySerializer, SellerSerializer, Car_brandSerializer,  Car_modelSerializer, Car_imageSerializer, CarSerializer

@api_view(['GET', ])
def country_list(request):
    countrys = Country.objects.all()
    serializer = CountrySerializer(countrys, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET', ])
def city_list(request):
    citys = City.objects.all()
    serializer = CitySerializer(citys, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def seller_list(request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def car_brand_list(request):
    car_brands = Car_brand.objects.all()
    serializer = Car_brandSerializer(car_brands, many=True)
    return Response(serializer.data)

@api_view(['GET', ])
def car_model_list(request):
    car_models = Car_model.objects.all()
    serializer = Car_modelSerializer(car_models, many=True)
    return Response(serializer.data)

# function car
@api_view(['GET', ])
def car_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

# function car detail
@api_view(['GET', ])
def car_detail(request, car_id):
    car = Car.objects.get(pk=int(car_id))
    serializer = CarSerializer(car)
    return Response(serializer.data)