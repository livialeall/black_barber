from django.shortcuts import render,redirect
from django import forms
from django.urls import reverse #consigo passar dados dentro da função para ela retornar uma url
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

#LOGIN DE USUARIO - FORMULARIO
class ClientLogin(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Favor escrever um email válido.'
        }
    ) 
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )
    
    class Meta:
        model = User
        #Campos que eu quero utilizar
        fields = ('email','password') #pega do meu model


#VIEW LOGIN DE NOVO USUARIO
def login(request):
    
    form = ClientLogin()
    
    if request.method == 'POST':
        
        form = ClientLogin(request.POST)
        #PEGO O EMAIL DIGITADO e VALIDO SE O EMAIL DIGITADO EXISTE NA DB
        email = form.__getitem__('email').value()
        email_db = Client.objects.filter(email=email)
        if email_db.exists() is False:
            messages.error(request,'Esse email não está cadastrado')
        else: 
            #SE EXISTIR O EMAIL EU VERIFICO SE É RELACIONADO COM A SENHA
            password = form.__getitem__('password').value()
            if email_db.filter(password=password).exists() is False:
                messages.error(request,'Essa senha não corresponde a esse email')
            else:
                return render(request,'user/user_page.html')
    
    
    site_title = 'Login'
    context = {
        'form' : form,
        'site_title' : site_title,

    }
    
    return render(request,'user/login.html',context)
