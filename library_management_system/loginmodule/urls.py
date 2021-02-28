from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'loginmodule'
urlpatterns = [
	path('',views.home,name='home'),
	path('home/',views.home,name='home'),
	path('register/',views.register,name='register'),
	path('login/',views.login,name='login'),
	path('welcome/',views.welcome,name='welcome'),
	path('failure/',views.failure,name='failure'),
	path('welcome/home.html',views.home,name='home'),
] 