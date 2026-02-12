from django.shortcuts import render
from flightapp.models import FlightDetails
from flightapp.serializer import FlightDetailsSerializer
from django.http import JsonResponse
from rest_framework import JSONParser
from django.views.decorators.csrf import csrf_exempt
from flightapp.serializer import FlightDetailsSerializer

# Create your views here.
@csrf_exempt
def FlightAPIViews(request):
    if request.method=='GET':
        flights=FlightDetails.objects.all()
        flight_data=FlightDetailsSerializer(flights,many=True)
        return JsonResponse(flight_data.data,safe=False)
    elif request.method=='POST':
        flights=JSONParser().parse(request)
        flight_serializer=FlightDetailsSerializer(data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse('Record added Sucessfully',safe=False)


