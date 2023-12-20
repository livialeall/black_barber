from django.shortcuts import render,redirect
from django import forms

from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm





def login(request):

    form = AuthenticationForm(request)
    site_title = 'Login'
    css_file = 'global/css/login.css'
    context = {
        'form' : form,
        'site_title' : site_title,
        'css_file':css_file
    }
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            return redirect('user:user_page',user_pk=user.pk)
            #FUTURAMENTE VAI REDIRECIONAR DIRETO PARA A PAGINA DO USUARIO
        else:
           messages.error(request,'Login Invalido')
           print('DEU ERRADO')
           return redirect('user:login')
           

    return render(request,'user/login.html',context)
