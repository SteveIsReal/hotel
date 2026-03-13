from rest_framework import generics, viewsets
from .serializer import CustomerSerializer, BookingSerializer, RoomSerializer, RegisterUser
from .models import Customer, Booking, Room
from django.contrib.auth.models import User

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        try:
            return Customer.objects.filter(user=self.request.user)
        except TypeError:
            return []

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValueError:
            return 0

class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        try:
            return Booking.objects.filter(user=self.request.user)
        except TypeError:
            return []

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValueError:
            return 0

class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        try:
            return Room.objects.filter(user=self.request.user)
        except TypeError:
            return []

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValueError:
            return 0

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUser
