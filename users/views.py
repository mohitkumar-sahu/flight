from django.shortcuts import render
from rest_framework.views import APIView
from users.models import Status
from rest_framework.response import Response
from users.serializer import StatusSerializer
from rest_framework import generics

# Create your views here.

# class AllStatusListView(APIView):
#     def get(self,request,*args,**kwargs):
#         qs=Status.objects.all()
#         serializer=StatusSerializer(qs,many=True)
#         return Response(serializer.data)
#     def post(self,request,*args,**kwargs):
#         qs=Status.objects.all()
#         serializer=StatusSerializer(qs,many=True)
#         return Response(serializer.data)
    
class AllStatusList(generics.ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

class StatusDetailView(generics.RetrieveAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'
