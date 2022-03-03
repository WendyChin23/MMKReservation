from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Account(models.Model):
    uid = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length = 50) #pwede ma unique, blank is equal to not required, Null is equal to null
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField()
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 50)

class Admin(models.Model):
    aid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)
    
class Reservation(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50, unique = True)
    phone = models.IntegerField()
    address = models.CharField(max_length = 100)
    zip = models.IntegerField()
    checkin_date = models.DateTimeField()
    checkin_time = models.TimeField()
    checkout_date = models.DateTimeField()
    checkout_time = models.TimeField()
