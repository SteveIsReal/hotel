from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room_type = models.CharField(max_length=100)
    room_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.room_type}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customers = models.ManyToManyField(Customer)
    book_date = models.DateTimeField()
    end_date = models.DateTimeField()
    room_type = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{[f"{i.first_name} {i.last_name}" for i in self.customers.all()]} / {self.room_type} ( {self.book_date} - {self.end_date} )'