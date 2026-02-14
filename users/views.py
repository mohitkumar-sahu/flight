from django.shortcuts import render
from rest_framework.views import APIView
from users.models import Status
from rest_framework.response import Response
from users.serializer import StatusSerializer
from rest_framework.generics import *

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
    
# class AllStatusList(ListAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer

# class StatusDetailView(RetrieveAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

# class StatusCreate(CreateAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer

# class StatusUpdateView(UpdateAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

# class StatusDelete(DestroyAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'

class StatusListCreateView(ListAPIView,mixins.CreateModelMixin):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StatusRetriveDestroyUpdateView(RetrieveAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)





