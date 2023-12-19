from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

#TIPOS DE SERVIÇOS
class Services(models.Model):
    male_cut = models.UniqueConstraint
    child_cut = models.UniqueConstraint
    shave = models.UniqueConstraint 

#DISPONIBILIDADE
class Appointments(models.Model):
    date = models.DateField()
    availability = models.BinaryField(unique_for_date=True,null=True,blank=True)
    services = models.ForeignKey(Services,on_delete=models.SET_NULL,null=True,blank=True)
    client = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)




