from xml.etree.ElementInclude import default_loader
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
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 50)

class Admin(models.Model):
    aid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)


class Conference(models.Model):
    cid = models.AutoField(primary_key = True)
    roomname = models.CharField(max_length = 100)
    roomtype = models.CharField(max_length = 100)
    price = models.IntegerField()
    pax = models.CharField(max_length = 100)
    isAvailable = models.BooleanField(default=True)


class Rooms(models.Model):
    rid = models.BigAutoField(primary_key = True)
    roomtype = models.CharField(max_length=100)
    date = models.DateField()
    email = models.CharField(max_length = 50, unique = True)
    day = models.CharField(max_length=100)
    cid = models.ForeignKey(Conference,to_field='cid', on_delete=models.CASCADE)


class Payment(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30)
    mop = models.CharField(max_length = 30)
    amount = models.IntegerField()


