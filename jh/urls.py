from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('Vila/',Vila , name="about"),
    path('Buk/',Buk ,name="buk"),
    path('Rum/',Rum , name="room"),
    path('Mit/',Mit , name="meeting"),
    path('Din/',Din , name="dinning"),
    path('contact/',contact , name="contact"),

]
