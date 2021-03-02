from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path('addBook/',views.addBook,name='addBook'),
   path('issueBook/',views.issueBook,name='issueBook'),
    path('returnBook/',views.returnBook,name='returnBook'),
] 