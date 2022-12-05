from django.urls import path
from .views import RoomListAPIView, RoomCreateAPIView, RoomDetailAPIView

urlpatterns = [
    path('', RoomListAPIView.as_view(), name='list'),
    path('create/', RoomCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', RoomDetailAPIView.as_view())
 
]
