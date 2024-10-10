from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room/', RoomView.as_view(), name='room'),  # Added trailing slash
    path('', RoomView.as_view(), name='home'),  # Root URL for home page
]
