from django.db import models

# Create your models here.
class FlightDetails(models.Model):
    flightname=models.CharField(max_length=100)
    flightId=models.CharField(max_length=100)
    start_point=models.CharField(max_length=100)
    endpoint=models.CharField(max_length=100)
    start_time=models.TimeField()
    #end_time=models.TimeField()
    flight_type=models.CharField(max_length=50)
    price=models.IntegerField()
    food_supply=models.CharField(max_length=50)
