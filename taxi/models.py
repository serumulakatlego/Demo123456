from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passanger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="passenger")
    #pass_fname
    #pass_sname
    #pass_cellphone
    #dest_spot
    #card_number
    #payment_method


class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="driver")
    #attribues to consider according to ERD
    #taxi_registrationID as a foreign key
    #driver_fname
    #driver_sname
    #driver_cellphone
    #driver_homeaddress
    #driver_email


class Taxi(models.Model):
    registration = models.CharField(max_length=200)
    manufature = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    #attribues to consider according to ERD
    #driver_licenceID
    #rank_name
    #passenger_id
    
   
class Destination:
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lan = models.FloatField()
    #attribues to consider according to ERD
    #dest_taxi_station
    #rank_id
    #price_id
      
    
class RankingTaxis(models.Model):
    taxi = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    destination = models.ForeignKey(User,on_delete=models.CASCADE)


class Rank(models.Model):
    name = models.CharField(max_length=200)
    ranking_taxis = models.ManyToManyField(RankingTaxis)
    #attribues to consider according to ERD
    

    def __str__(self) -> str:
        return self.name

