from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'loginmodule'
urlpatterns = [
   path('',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('welcome/',views.welcome,name='welcome'),
   path('logout/',views.logout,name='logout'),
]
