from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

#USUARIO
class Client(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Nome',null=False,blank=False)
    last_name = models.CharField(max_length=50,verbose_name='Sobrenome',null=False,blank=False)
    phone = models.CharField(max_length=50,verbose_name='Contato')
    email = models.EmailField(max_length=250,blank=True)
    picture = models.ImageField(blank=True,null=True,upload_to='pictures/%Y/%m')
    
    #marcações

