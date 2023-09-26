from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer, RestaurantStatisticsSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.gis import geos
from django.contrib.gis.measure import Distance
from django.db.models import Avg,Count,StdDev



@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/delete/pk'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_restaurant(request):
    restaurant = RestaurantSerializer(data=request.data)
    restaurant.location=geos.Point(restaurant.lng,restaurant.lat)

    # validando si existe
    if Restaurant.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This restaurant already exists')

    if restaurant.is_valid():
        restaurant.save()
        return Response(restaurant.data)
    else:
        return Response(status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def view_restaurant(request):
    if request.query_params:
        restaurants = Restaurant.objects.filter(**request.query_params.dict())
    else:
        restaurants = Restaurant.objects.all()

    if restaurants:
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    data = RestaurantSerializer(instance=restaurant, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_409_CONFLICT)

@api_view(['DELETE'])
def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def statistics_restaurant(request):
    lat=request.GET.get('latitude')
    lng=request.GET.get('longitude')
    radius=request.GET.get('radius')
    center=geos.Point(lng,lat)
    restaurants=get_statistics(center,radius)
    if restaurants:
        serializer = RestaurantStatisticsSerializer(restaurants)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

def get_statistics(center,radius):
    return Restaurant.objects.filter(
    location__distance_lt=(center,Distance(m=radius))).aggregate(
    count=Count('id'), avg=Avg('rating'), std=StdDev('rating'))
