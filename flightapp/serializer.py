from rest_framework import serializers
from flightapp.models import FlightDetails

class FlightDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlightDetails
        fields='__all__'