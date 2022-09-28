from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passanger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="passenger")


class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="driver")


class Taxi(models.Model):
    registration = models.CharField(max_length=200)
    manufature = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

class Destination:
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lan = models.FloatField()
    
class RankingTaxis(models.Model):
    taxi = models.ForeignKey(Taxi,on_delete=models.CASCADE)
    destination = models.ForeignKey(User,on_delete=models.CASCADE)




class Rank(models.Model):
    name = models.CharField(max_length=200)
    ranking_taxis = models.ManyToManyField(RankingTaxis)

    def __str__(self) -> str:
        return self.name

