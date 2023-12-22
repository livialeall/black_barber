from django.shortcuts import render,get_object_or_404,redirect
from user.models import Services,TimeSlot
from user.form_appointment import AppointmentForm
from . import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from mplcursors import cursor
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.urls import reverse #consigo passar dados dentro da função para ela retornar uma url
    

#ACESSANDO PAGINA DO USUARIO - Inicial
@login_required(login_url='user:login')
def user_page(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    user_pk = user.pk
    site_title = f'{user.first_name} {user.last_name}'
    css_file = 'global/css/user_page.css'
    services = Services.objects.all()
    user_appointment = TimeSlot.objects.filter(user=user_pk)
    print(user_appointment)
    context = {
        'user' : user.__str__().capitalize,
        'site_title' : site_title,
        'services': services,
        'user_pk' : user.pk,
        'css_file':css_file,
        'user_appointment':user_appointment
        
    }
    return render(request,'user/user_page.html',context)
    

@login_required(login_url='user:login')
def new_appointment(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    user_pk = user.pk
    css_file = 'global/css/user_page.css'
    form = AppointmentForm()
    site_title = 'Novo Agendamento'
    services = Services.objects.all()
    
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
        'services': services,
        'css_file':css_file,
        'user_pk' : user.pk,
    }
    return render(request,'user/new_appointment.html',context)
   
   
    
@login_required(login_url='user:login')
def loyalty_programme(request,user_pk):
    css_file = 'global/css/user_page.css'
    site_title = 'Seu Programa de Fidelidade'

    user = get_object_or_404(User,pk=user_pk)
    user_pk = user.pk
    user_appointment = TimeSlot.objects.filter(user=user_pk)
    user_appointment_valid_for_the_programme = TimeSlot.objects.filter(user=user_pk).exclude(services=560)
    
    cuts_to_win = 6
    user_appoints_qt = user_appointment_valid_for_the_programme.__len__()
    cuts_missing = cuts_to_win - user_appoints_qt
    
    # Seus dados para o gráfico de rosca (exemplo)
    labels = ['','']
    sizes = [cuts_missing,user_appoints_qt]

    # Criar o gráfico de rosca (Donut Chart) com Matplotlib
    colors = ['#D9D9D9', '#628C45']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, startangle=90, wedgeprops=dict(width=0.3), pctdistance=0.85,colors=colors)
    ax.axis('equal')  # Assegurar que o gráfico é circular
    
    # Adicionar o valor de porcentagem ao centro do Donut Chart
    center_text = f"{((user_appoints_qt/cuts_to_win)*100):.1f}%"
    ax.text(0, 0, center_text, ha='center', va='center', fontsize=24, fontweight='bold', color='#628C45',fontname='Lato')

    # Salvar o gráfico em BytesIO
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Converter a imagem para base64
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    
    context = {
        'user' : user,
        'site_title' : site_title,
        'css_file':css_file,
        'user_pk' : user.pk,
        'user_appointment':user_appointment,
        'cuts_missing':cuts_missing,
        'image_base64':image_base64
    }
    return render(request,'user/loyalty_programme.html',context)