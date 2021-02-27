from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reader

def login(request):
    return render(request,'login.html')

def failure(request):
    return render(request,'failure.html')
def register(request):
    if request.method == "POST" :
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['repassword']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        #check the data is entered or not by the user
        if username != '' and password1 != '' and password2 != '' and email != '' and first_name != '' and last_name != '':
            #check password and repassword are same or not
            if password1 == password2:
                #if both are same then forward procced
                if Reader.objects.filter(username = username).exists():
                    messages.info(request,'username already taken')
                    return render(request,'register.html')
                elif Reader.objects.filter(email = email).exists():
                    messages.info(request,'email already taken')
                    return render(request,'register.html')
                else :
                    user = Reader(username = username , password = password1,
                                                        first_name = first_name , last_name = last_name,
                                                        email = email)
                    user.save()
                    return redirect('/login')
                    
            #if passwords are not match then again render register pagr                               
            else:
                messages.info(request,"password does not match")
                return redirect('register')
        else:
            messages.info(request,"please enter the data")
            messages.info(request,"all fields are must required")
            return render(request,'register.html')

    else:
         return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def welcome(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['userpassword']
        #check user is register or not
        if Reader.objects.filter(username = username).exists() and Reader.objects.filter(password = password).exists():
             return render(request,'welcome.html')
        #user is  register then value of user is not None
        else:
            #login access to user
            messages.info(request,"Invalid username or password")
            return redirect('/login')
    else:
        return render(request,'login.html')
    
    