from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    # path("/welcome",views.welcome,name="welcome"),
    
] 