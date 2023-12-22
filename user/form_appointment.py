from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User #model para user
from . import models
from user.models import Services,TimeSlot
from django.utils import timezone

class AppointmentForm(forms.ModelForm):  
    def clean(self):
        date = self.cleaned_data.get('date')
        time = self.cleaned_data.get('time')
        date_db = TimeSlot.objects.filter(date=date)
        
        if date_db.filter(time=time): #se a hora que passaram no form existe na db
            self.add_error(
                'time',
                ValidationError('Esse horário já está ocupado, favor escolher um horário disponível',code='invalid')
            )
        super().clean()
    
    
    picture = forms.ImageField(required=False,
        widget=forms.FileInput(
            attrs={
                'accept':'image/*', #qualquer imagem
    
            }  
        ),
        label = 'Referências de corte/barba'
        )
    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y',attrs={'type': 'date'}),
        input_formats=['%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y'],
    )
    
    HORARIOS = [
        ('8','8H'),
        ('9','9H'),
        ('10','10H'),
        ('11','11H'),
        ('12','12H'),
        ('14','14H'),
        ('15','15H'),
        ('16','16H'),
        ('17','17H'),
        ('18','18H'),
    ]
    time = forms.ChoiceField(choices=HORARIOS, widget=forms.Select)
    
    
    class Meta:
        model = TimeSlot
        #Campos que eu quero utilizar
        fields = ('services','date','time','picture') #pega do meu model
    
     