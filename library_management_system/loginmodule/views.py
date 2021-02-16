from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def login(request):
    return render(request,'login.html')

def register(request):
    global user
    if request.method == "POST" :
        #check password and repassword are same or not
        if request.POST['password'] == request.POST['repassword']:
            #if both are same then forward procced
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'error':"user already exist"})
            except User.DoesNotExist:
                user = User.objects.create(username=request.POST['username'],
                                           password=request.POST['password'],
                                           email = request.POST['email'],
                                           first_name = request.POST['fname'],
                                           last_name = request.POST['lname'])
                return redirect(login)
                
         #if passwords are not match then again render register pagr                               
        else:
             return render(request,'register.html',{'error':"password don't match"})

    else:
         return render(request,'register.html')

def home(request):
    return render(request,'home.html')
