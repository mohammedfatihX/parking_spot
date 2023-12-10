# parking_app/models.py

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)


class ParkingPlace(models.Model):
    name = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)
    reserved_by_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    date_reserved = models.DateTimeField(null=True, blank=True)
