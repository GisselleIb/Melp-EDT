from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Restaurant(models.Model):
    id = models.TextField(max_length=255,primary_key=True)
    rating = models.IntegerField(
            default=0,
            validators=[MaxValueValidator(4), MinValueValidator(0)])
    name = models.TextField(max_length=255)
    site = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    street = models.TextField(max_length=255)
    city = models.TextField(max_length=255)
    state = models.TextField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    location = models.PointField(geography=True,default=Point(0.0,0.0))


    def __str__(self):
        return self.name
