from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User,auth
from .models import Reader

superuser_username = "admin"
superuser_password = "admin" 

def login(request):
    if request.session.get('username') == None:
        return render(request,'loginmodule/login.html')
    else:
        return redirect('loginmodule:welcome')

def register(request):
    if request.method == "POST" :
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['repassword']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
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
                return redirect(reverse("loginmodule:login"))
                
        #if passwords are not match then again render register pagr                               
        else:
            messages.error(request,"password does not match")
            return render(request,'loginmodule/register.html')
    else:
         return render(request,'loginmodule/register.html')

def home(request):
    if request.session.get('username') == None:
        return render(request,'loginmodule/home.html')
    else:
        return redirect(reverse("loginmodule:welcome"))

def welcome(request):
    if request.session.get('username') == None:
        if request.method == "POST":
            # analyse the form
            username=request.POST['username']
            password=request.POST['password']
            try:
                superUser = request.POST['superuser']
            except:
                superUser = None
            if superUser == "superuser":
                if username == superuser_username and password == superuser_password:
                    request.session['superuser'] = True
                    # return redirect(reverse("loginmodule:welcome"))
                    return render(request,"loginmodule/welcome.html")
                else:
                    messages.error(request,"You'r not authorize")
                    return render(request,"loginmodule/login.html")
            else:
                #check user is register or not
                if Reader.objects.filter(username = username).exists() and Reader.objects.filter(password = password).exists():
                    request.session['username'] = username
                    return render(request,'loginmodule/welcome.html')
                #user is  register then value of user is not None
                else:
                    #login access to user
                    messages.error(request,"Invalid username or password")
                    return redirect(reverse("loginmodule:login"))
        else:
            # first login
            return redirect(reverse("loginmodule:login"))
    else:
        return render(request,'loginmodule/welcome.html')
    
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'superuser' in request.session:
        del request.session['superuser']
    messages.success(request,'You are logged out!')
    return redirect(reverse('loginmodule:login'))