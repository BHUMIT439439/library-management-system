from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Reader

def login(request):
    if request.session.get('username') == None:
        return render(request,'loginmodule/login.html')
    else:
        return redirect('loginmodule:welcome')

def failure(request):
    return render(request,'loginmodule/failure.html')

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
                    messages.error(request,'username already taken')
                    return render(request,'loginmodule/register.html')
                elif Reader.objects.filter(email = email).exists():
                    messages.error(request,'email already taken')
                    return render(request,'loginmodule/register.html')
                else :
                    user = Reader(username = username , password = password1,
                                                        first_name = first_name , last_name = last_name,
                                                        email = email)
                    user.save()
                    return redirect('/login')
                    
            #if passwords are not match then again render register pagr                               
            else:
                messages.error(request,"password does not match")
                return redirect('loginmodule/register')
        else:
            messages.error(request,"please enter the data")
            messages.error(request,"all fields are must required")
            return render(request,'loginmodule/register.html')

    else:
         return render(request,'loginmodule/register.html')

def home(request):
    return render(request,'loginmodule/home.html')

def welcome(request):
    if request.session.get('username') == None:
        if request.method == "POST":
            username=request.POST['username']
            password=request.POST['userpassword']
            #check user is register or not
            if Reader.objects.filter(username = username).exists() and Reader.objects.filter(password = password).exists():
                request.session['username'] = username
                return render(request,'loginmodule/welcome.html')
            #user is  register then value of user is not None
            else:
                #login access to user
                messages.error(request,"Invalid username or password")
                return redirect('/login')
        else:
            return render(request,'loginmodule/login.html')
    else:
        return render(request,'loginmodule/welcome.html')
    
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    messages.success(request,'You are logged out!')
    return render(request,'loginmodule/login.html')