from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'loginmodule'
urlpatterns = [
<<<<<<< HEAD
   path('',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('welcome/',views.welcome,name='welcome'),
   path('failure/',views.failure,name='failure'),
=======
	path('',include(loginmodule.views)),
>>>>>>> fa490791413aa8d5606537dc126b810cf856fe5c
] 