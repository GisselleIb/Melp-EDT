from api.models import Restaurant
from django.contrib.gis.geos import Point
import csv

def run():
    with open('api/restaurantes.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Restaurant.objects.all().delete()

        for row in reader:
            restaurant = Restaurant(id=row[0],rating=row[1],
                                    name=row[2],site=row[3],
                                    email=row[4],phone=row[5],
                                    street=row[6],city=row[7],
                                    state=row[8],lat=row[9],
                                    lng=row[10],location=Point(float(row[10]),float(row[9])))
            restaurant.save()
