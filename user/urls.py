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
    #PAGINA DO USUARIO
    path('user/<int:user_pk>/user_page',views.user_page,name='user_page'),
    #NOVA MARCAÇÃO
    path('user/<int:user_pk>/new_appoint',views.new_appointment,name='new_appoint'),
    #PROGRAMA DE FIDADELIDADE
    path('user/<int:user_pk>/loyalty_programme',views.loyalty_programme,name='loyalty_programme'),
]