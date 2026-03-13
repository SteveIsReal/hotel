from rest_framework import serializers
from .models import Customer, Room, Booking
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'phone']
        read_only_fields = ['user']
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_type', 'room_description']
        read_only_fields = ['user']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['customers','book_date','end_date','room_type']
        read_only_fields = ['user']

class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, data):
        user = User.objects.create_user(
            username = data['username'],
            password=data['password'],
            email = data.get('email', '')
        )
        return user
