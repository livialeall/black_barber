from django.shortcuts import render,redirect
from django.urls import reverse
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
import pdb


def index(request):
    site_title = 'Pagina inicial'
    context = {
        'site_title' : site_title
    }
    return render(request,'user/index.html',context)


#CADASTRO DE NOVO USUARIO - FORMULARIO
#SOBREESCREVE O MEU MODEL
class ClientRegister(UserCreationForm):
    first_name = forms.CharField(max_length=255,required=True)
    last_name = forms.CharField(max_length=255,required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        #Campos que eu quero utilizar do db do usario
        fields = ('first_name','last_name','username','email','password1','password2') #pega do meu model
        
        #SE TENTAREM CRIAR OUTRA CONTA COM UM MEIAL QUE JA EXISTE
        def clean_email(self):
            email = self.cleaned_data.get('email')
        
            if User.objects.filter(email=email).exists(): #se o email que passaram no form existe na db
                self.add_error(
                'email',
                ValidationError('Ja existe um usuario com esse email',code='invalid')
                )
            
            return email



#VIEW CADASTRO DE NOVO USUARIO
def sign_up_form(request):
    
    site_title = 'Cadastro'
    form = ClientRegister()
    form_action = reverse('user:sign_up_form')
    
    #se for um formualrio do tipo post e nao apenas uma renderização tipo GET eu salvo na db realizo o envio os dados do POST para o form
    if request.method =='POST':
        form = ClientRegister(request.POST)
        print('step')

       
        if form.is_valid():
            print('step')
            form.save()
            print('step')
            return redirect('user:index') #FUTURAMENTE VAI REDIRECIONAR DIRETO PARA A PAGINA DO USUARIO

    
    context = {
        'site_title' : site_title,
        'form':form,
        'form_action':form_action

  
    }
    return render(request,'user/sign_up_form.html',context)




