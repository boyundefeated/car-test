from django.conf.urls import url

from . import views, restapi

urlpatterns = [

    url(r'^$', views.test, name='test'),
    url(r'^api/country/$', restapi.country_list, name='api_country'),
    url(r'^api/city/$', restapi.city_list, name='api_city'),
    url(r'^api/seller/$', restapi.seller_list, name='api_seller'),
    url(r'^api/car/$', restapi.car_list, name='api_car'),
    url(r'^api/car/(?P<car_id>[0-9]+)/$', restapi.car_detail, name='api_car_detail'),
]