from django.db.models import fields
from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','rating','name','site','email',
                  'phone','street','city','state','lat','lng')

class RestaurantStatisticsSerializer(serializers.ModelSerializer):
    avg = serializers.FloatField()
    count = serializers.IntegerField()
    std = serializers.FloatField()
    class Meta:
        model = Restaurant
        fields = ('count','avg','std')
