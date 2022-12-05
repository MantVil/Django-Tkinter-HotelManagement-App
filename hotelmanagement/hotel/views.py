from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Room
from .serializers import RoomListSerializer, RoomCreateSerializer, RoomDetailSerializer
# Create your views here.

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer

class RoomDetailAPIView(RetrieveAPIView):
    queryset =  Room.objects.all()
    serializer_class = RoomDetailSerializer

# class RoomUpdateAPIView(UpdateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomUpdateSerializer
