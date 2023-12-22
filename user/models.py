from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

#TIPOS DE SERVIÇOS
class Services(models.Model):
    services_code = models.CharField(max_length=100,blank=True,null=True)
    services_name = models.CharField(max_length=100,blank=True,null=True)
    #INCLUIR VALORES
    services_amount = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.services_name} - R${self.services_amount}"
    

#DISPONIBILIDADE
class TimeSlot(models.Model):
    services = models.ForeignKey(Services,on_delete=models.CASCADE) #temporario
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=255)
    picture = models.ImageField(null=True,blank=True)
    is_availabe = models.BooleanField(default=False)
    #picture
    
    def __str__(self):
        return f"{self.services.services_name} - Dia :{self.date.strftime('%Y-%m-%d')} Hora: {self.time}"
    




