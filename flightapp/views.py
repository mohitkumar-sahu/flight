from django.shortcuts import render
from flightapp.models import FlightDetails
from flightapp.serializer import FlightDetailsSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from flightapp.serializer import FlightDetailsSerializer

# Create your views here.
@csrf_exempt
def FlightAPIViews(request,id=0):
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
        
    elif request.method=="PUT":
        flights=JSONParser().parse(request)
        old_record=FlightDetails.objects.get(id=id)
        flight_serializer = FlightDetailsSerializer(old_record, data=flights)
        if flight_serializer.is_valid():
            flight_serializer.save()
        return JsonResponse('Record updated Sucessfully',safe=False)
    
    elif request.method=='DELETE':
        flights=FlightDetails.objects.get(id=id)
        flights.delete()
        return JsonResponse('Record Deleted Sucessfully',safe=False)




