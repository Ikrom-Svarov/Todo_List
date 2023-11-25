from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import List
from .serializers import ListSerializers

# Create your views here.
class ApiList(ListAPIView):
    queryset = List.objects.all()
    serializer_class  = ListSerializers


class CreateApi(CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializers


class RetrieveApi(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializers