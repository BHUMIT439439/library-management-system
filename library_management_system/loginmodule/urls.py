from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'loginmodule'
urlpatterns = [
	path('',include(loginmodule.views)),
] 