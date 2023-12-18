from django.urls import path
from user import views #importa o package inicializado por __init__ como se fosse o arquivo views.py

app_name = 'user'

urlpatterns = [
    #PAGINA INICIAL
    path('',views.index,name='index'),
    #CADASTRO DE NOVO USUARIO
    path('sign_up_form/',views.sign_up_form,name='sign_up_form'),
    #LOGIN DE USUARIO
    path('login/',views.login,name='login'),
    
   
]