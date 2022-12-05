from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Room
from .serializers import RoomListSerializer, RoomCreateSerializer
# Create your views here.

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer