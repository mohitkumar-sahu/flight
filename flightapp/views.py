from django.shortcuts import render
from flightapp.models import FlightDetails
from flightapp.serializer import FlightDetailsSerializer
from django.http import JsonResponse

# Create your views here.
def FlightAPIViews(request):
    if request.method=='GET':
        flights=FlightDetails.objects.all()
        flight_data=FlightDetailsSerializer(flights,many=True)
        return JsonResponse(flight_data.data,safe=False)
    elif request.method=='POST':
        pass
