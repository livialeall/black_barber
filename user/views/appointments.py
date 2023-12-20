from django.shortcuts import render,get_object_or_404,redirect
from user.models import Services,TimeSlot
from user.form_appointment import AppointmentForm
from . import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse #consigo passar dados dentro da função para ela retornar uma url

#ACESSANDO PAGINA DO USUARIO - Inicial
@login_required(login_url='user:login')
def user_page(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    user_pk = user.pk
    site_title = f'{user.first_name} {user.last_name}'
    css_file = 'global/css/user_page.css'
    services = Services.objects.all()
    print(services)
    context = {
        'user' : user.__str__().capitalize,
        'site_title' : site_title,
        'services': services,
        'user_pk' : user.pk,
        'css_file':css_file
        
    }
    return render(request,'user/user_page.html',context)
    

@login_required(login_url='user:login')
def new_appointment(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    
    form = AppointmentForm()
    site_title = 'Novo Agendamento'
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('user:user_page',user_pk=user.pk) #pega o user.id
  
    context = {
        'user' : user,
        'site_title' : site_title,
        'form':form,
    }
    return render(request,'user/new_appointment.html',context)
    
