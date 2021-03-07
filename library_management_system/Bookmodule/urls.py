from django.urls import path
from django.contrib import admin
from . import views

app_name = 'Bookmodule'
urlpatterns = [
   path('addBook/',views.addBook,name='addBook'),
   path('issueBook/',views.issueBook,name='issueBook'),
   path('returnBook/',views.returnBook,name='returnBook'),
   path('removeBook/',views.removeBook,name='removeBook'),
   path('showFine/',views.showFine,name='showFine'),
] 