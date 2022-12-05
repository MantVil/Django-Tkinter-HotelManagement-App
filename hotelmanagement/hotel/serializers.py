from rest_framework.serializers import ModelSerializer
from .models import Room

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'room_num',
            'check_in',
            'guest',
            'check_in',
            'check_out'
        ]