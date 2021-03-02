from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('welcome/',views.welcome,name='welcome'),
   path('failure/',views.failure,name='failure'),
] 