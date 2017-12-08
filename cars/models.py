from django.db import models
from authentication.models import User
from datetime import datetime

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=45)
    currency_unit = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=45)
    country = models.ForeignKey(Country, related_name='citys', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Seller(models.Model):
    # User: user_name, pw, email, first_name, last_name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    location_pin = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    type = models.BooleanField(default=True)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user

class Car_brand(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Car_model(models.Model):
    name = models.CharField(max_length=45)
    brand = models.ForeignKey(Car_brand, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    condition = models.CharField(max_length=45)
    year = models.IntegerField()
    trim = models.CharField(max_length=45)
    car_model = models.CharField(max_length=45)
    body_style = models.CharField(max_length=45)
    transmission = models.IntegerField()
    fuel = models.CharField(max_length=45)
    feature = models.TextField()
    cylinder = models.IntegerField()
    color_internal = models.CharField(max_length=45)
    color_external = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    kilometer = models.IntegerField()
    user = models.ForeignKey(Seller, on_delete=models.CASCADE)
    car_brand = models.CharField(max_length=45)
    describe = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

def car_directory_path(instance, filename):
    return 'car_{0}/{1}'.format(instance.car.id, filename)

class Car_image(models.Model):
    # image = url
    image = models.ImageField(upload_to=car_directory_path)
    car = models.ForeignKey(Car,related_name='car_images', on_delete=models.CASCADE)
