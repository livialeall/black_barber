from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


#SERVICOS - CORTES FEITOS PELA BARBEARIA
class Services(models.Model):
    ...

#DIA/HORA DISPONIVEIS
class Timetable(models.Model):
    ...    

#MARCAÇÕES

class Appointment(models.Model):
    ...

    #marcações

