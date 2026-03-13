from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Room(models.Model):
    room_type = models.CharField(max_length=100)
    room_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.room_type}'

class Booking(models.Model):
    customers = models.ManyToManyField(Customer)
    book_date = models.DateTimeField()
    end_date = models.DateTimeField()
    room_type = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.customers} / {self.room_type} ( {self.book_date} - {self.end_date} )'