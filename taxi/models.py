from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passanger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="passenger")
    pass_fname = models.CharField(max_length=200)
    pass_sname = models.CharField(max_length=200)
    pass_cellphone = models.CharField(max_length=200)
    dest_spot = models.CharField(max_length=200)
    card_number = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=200)


class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="driver")
    taxi_registrationID = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    driver_fname = models.CharField(max_length=200)
    driver_sname = models.CharField(max_length=200)
    driver_cellphone = models.CharField(max_length=200)
    driver_homeaddress = models.CharField(max_length=200)
    driver_email = models.CharField(max_length=200)


class Taxi(models.Model):
    registration = models.CharField(max_length=200)
    manufature = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    driver_licenceID = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    rank_name = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    
   
class Destination:
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lan = models.FloatField()
    dest_taxi_station = 
    rank_id = models.CharField(max_length=200)
    price_id
      
    
class RankingTaxis(models.Model):
    taxi = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    destination = models.ForeignKey(User,on_delete=models.CASCADE)


class Rank(models.Model):
    name = models.CharField(max_length=200)
    ranking_taxis = models.ManyToManyField(RankingTaxis)
    
class paymentMethod(models.Model):
    pay_methodID = user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="paymentMethod")
    pay_option = models.CharField(max_length=200) 
 
    

    def __str__(self) -> str:
        return self.name

