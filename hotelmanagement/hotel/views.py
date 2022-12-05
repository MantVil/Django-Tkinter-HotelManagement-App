from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomListSerializer
# Create your views here.

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer