from django.shortcuts import render,redirect
from django import forms
from django.urls import reverse #consigo passar dados dentro da função para ela retornar uma url
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from user.models import Client
from django.contrib.auth import password_validation



def index(request):
    site_title = 'Pagina inicial'
    context = {
        'site_title' : site_title
    }
    return render(request,'user/index.html',context)


#CADASTRO DE NOVO USUARIO - FORMULARIO
class ClientRegister(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'required': 'Favor escrever um nome válido.'
        }
    )
    
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        error_messages={
            'required': 'Favor escrever um nome válido.'
        }
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )
    confirmation_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Client
        #Campos que eu quero utilizar
        fields = ('first_name','last_name','phone','email','password','confirmation_password') #pega do meu model



#VIEW CADASTRO DE NOVO USUARIO
def sing_up_form(request):
    site_title = 'Cadastro'
    form = ClientRegister()
    form_action = reverse('user:sign_up_form')
    
    #se for um formualrio do tipo post e nao apenas uma renderização tipo GET eu salvo na db realizo o envio os dados do POST para o form
    if request.method =='POST':
        form = ClientRegister(resquest.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Usuario registrado com sucesso')
            return redirect('contact:index') #FUTURAMENTE VAI REDIRECIONAR DIRETO PARA A PAGINA DO USUARIO
    context = {
        'site_title' : site_title,
        'form':form,
        'form_action':form_action
    }
    return render(request,'user/sign_up_form.html',context)

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
        model = Client
        #Campos que eu quero utilizar
        fields = ('email','password') #pega do meu model


#VIEW LOGIN DE NOVO USUARIO
def login(request):
    form = ClientLogin()
    form_action = reverse('user:login')
    if request.method =='POST':
        form = ClientLogin(resquest.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contact:index') #FUTURAMENTE VAI REDIRECIONAR DIRETO PARA A PAGINA DO USUARIO
    site_title = 'Login'
    context = {
        'form' : form,
        'site_title' : site_title,
        'form_action':form_action
    }
    return render(request,'user/login.html',context)
