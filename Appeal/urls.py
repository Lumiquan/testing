from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.team, name='team'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('Signup/', views.Signuppage, name='Signuppage'),
    path('Reset/', views.Resetpage, name= 'Resetpage'),
    path('Appealtable/', views.Appeal_table, name='Appeal_table')
]